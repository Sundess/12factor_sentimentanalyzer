# Sentiment Analyzer API Docs

## 🧪 API Endpoints

The application’s API endpoints are defined in main.py under the app directory, using the FastAPI framework to handle HTTP requests and responses efficiently.

`GET /`

Returns a welcome message:

```json
{
  "message": "Welcome to Homepage"
}
```

`POST /analyze/`

Analyzes user-provided text and returns the sentiment.

**Request Body:**

```json
{
  "text": "I love this product!"
}
```

**Response:**

```json
{
  "text": "I love this product!",
  "sentiment": "Positive"
}
```

A background Celery task is triggered to save this information in the database.

---

## 🧠 Sentiment Analysis Engine

- Implemented in `sentiment_analyzer.py`
- Uses Groq LLaMA 4 model with system instructions to return:

  - `positive`
  - `negative`
  - `neutral`

---

## 🛠 Celery Background Task

### Task Location

`workers/tasks.py`

### Function

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
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### docker-compose.yml

```yaml
version: "3.9"
services:
  web:
    build: .
    container_name: fastapi_web
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - redis
      - db

  worker:
    build: .
    container_name: celery_worker
    command: celery -A workers.db_saver_celery_worker worker --loglevel=info
    env_file:
      - .env
    depends_on:
      - redis
      - db

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  db:
    image: postgres:14
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
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
