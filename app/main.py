"""
A FastApi app for sentiment analysis
"""

import os

from fastapi import FastAPI
from pydantic import BaseModel
from workers.tasks import save_sentiment

from app.sentiment_analyzer import sentiment_analyzer


class SentimentText(BaseModel):
    """Model for Getting sentiment text"""

    text: str


app = FastAPI()


@app.get("/")
def root():
    """Return Main Home Page"""
    return {"message": "Welcome to Homepage"}


@app.post("/analyze/")
def analyze_sentiment(sentiment_text: SentimentText):
    """
    Analyze the text get by getting the text from the user

    Return Json data as {"message" : "sentiment"} Positive Negative or Neutral
    """
    text = sentiment_text.text

    sentiment = sentiment_analyzer(text=text)

    print("BROKER_URL =", os.getenv("BROKER_URL"))

    # Enqueue async save task
    save_sentiment.delay({"text": text, "result": sentiment})

    return {"text": text, "sentiment": sentiment}
