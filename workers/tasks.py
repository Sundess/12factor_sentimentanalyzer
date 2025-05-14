"""
Saves the generated result in database
"""

import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

from .db_saver_celery_worker import celery_app

load_dotenv()


@celery_app.task(name="app.task.save_sentiment")
def save_sentiment(data):
    """
    Saves the generated result in database
    """

    DATABASE_URL = os.getenv("DATABASE_URL")
    try:
        engine = create_engine(DATABASE_URL)
    except Exception as e:
        print(e)

    metadata = MetaData()
    sentiments = Table(
        "sentiments",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("text", String),
        Column("result", String),
    )
    metadata.create_all(engine)
    try:
        with engine.connect() as conn:
            conn.execute(sentiments.insert().values(text=data["text"], result=data["result"]))
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Saved to database successfully.")  # 👈 Confirmation print
