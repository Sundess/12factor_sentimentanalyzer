# Key Components

## 🧠 Sentiment Analysis Endpoint

Location: `app/main.py`

#### Function

```
@app.post("/analyze/")
def analyze_sentiment(sentiment_text: SentimentText):
  # Allows users to send request to server.
```

## 🛠️ Sentiment Analysis Engine

Location: `app/sentiment_analyzer.py`

#### Function

```
def sentiment_analyzer(text):
    """
    Take text as input and analyzer the text.
    Categories it into Positive, Negative or Neutral & returns it.
    """
```

- Uses Groq LLaMA 4 model with system instructions to return:
  - `positive`
  - `negative`
  - `neutral`

---

## 📝 Celery Background Task

Location: `workers/tasks.py`

#### Function

```python
@celery_app.task(name="app.task.save_sentiment")
def save_sentiment(data):
    # Connects to DATABASE_URL and saves the text + sentiment
```

Database table: `sentiments(id, text, result)` is created if it doesn't exist.

---

## 🐳 Dockerization

### Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

### docker-compose.yml

```yaml
version: "3.8"
services:
  web:
    build: .
    container_name: fastapi_web
    ports:
      - "8000:8000"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
      - BROKER_URL=redis://redis:6379/0
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/mydatabase
    depends_on:
      - redis
      - db
    # no volumes for prod; add if you want live reload
    # volumes:
    #   - .:/app

  worker:
    build: .
    container_name: celery_worker
    command: >
      celery -A workers.db_saver_celery_worker worker --loglevel=info
    environment:
      - BROKER_URL=redis://redis:6379/0
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/mydatabase
    depends_on:
      - redis
      - db
      - web

  redis:
    image: redis:7-alpine
    container_name: redis
    ports:
      - "6379:6379"

  db:
    image: postgres:13-alpine
    container_name: postgres
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
    # volumes:
    #   - pgdata:/var/lib/postgresql/data
# volumes:
#   pgdata:
```

---

## 🧪 Running the Project

```bash
# Build and start containers
$ docker-compose up --build
```

Visit: [http://localhost:8000/](http://localhost:8000/) to test the API.

To tail logs:

```bash
docker-compose logs -f worker
docker-compose logs -f web
```

To bring services down:

```bash
docker-compose down
```

---

## 📚 Development Notes

- **Celery** loads `.env` using `dotenv.load_dotenv()`.
- **PostgreSQL table** is created dynamically inside the task.
- **Groq API** requires an active key with appropriate usage limits.
- No volume persistence is currently configured.

---

## 🧾 License & Attribution

- LLaMA 4 by Meta AI (via Groq)
- FastAPI licensed under MIT
- This project template was generated with ❤️ and Docker 🐳
