# Sentiment Analyzer API Docs

Welcome to the official documentation for the **Sentiment Analyzer API**, a FastAPI application powered by Groq's LLaMA 4 model for sentiment analysis. It leverages **Celery** for background task processing and **PostgreSQL** for data storage. Docker is used for environment orchestration.

---

## 🚀 Overview

### Tech Stack

- **Framework**: FastAPI
- **Background Jobs**: Celery
- **Message Broker**: Redis
- **Database**: PostgreSQL
- **AI Model**: Groq Meta-LLaMA-4 (Scout)
- **Environment Variables**: `.env`

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
