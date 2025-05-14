# Setting Project Locally

For this you need to have git and docker installed locally in you machine.

## Local Setup

```
# Cloning the repository

git clone https://github.com/Sundess/12factor_sentimentanalyzer
cd 12factor_sentimentanalyzer

# Creating and Activating Virtual Environment

python -m venv env
source env/bin/activate

# Installing dependencies

pip install -r requirements.txt

# Running docker-compose for building the application

docker compose up --build
```

---

## 📂 Folder Structure

```plaintext
root/
├── app/
│   ├── main.py                  # FastAPI app and endpoint definitions
│   └── sentiment_analyzer.py   # Calls Groq API to analyze sentiment
├── workers/
│   ├── db_saver_celery_worker.py  # Celery app initialization
│   └── tasks.py                   # Task to save data to PostgreSQL
├── .env                        # Environment variables
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image setup
├── docker-compose.yml          # Multi-container orchestration
└── docs/                       # MkDocs source
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the root directory with the following keys:

```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=postgresql://postgres:postgres@db:5432/mydatabase
BROKER_URL=redis://redis:6379/0
```

These will be used across the FastAPI app, Celery, and Groq client.

---

## 🧪 API Endpoints

### `GET /`

Returns a welcome message:

```json
{
  "message": "Welcome to Homepage"
}
```

### `POST /analyze/`

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
