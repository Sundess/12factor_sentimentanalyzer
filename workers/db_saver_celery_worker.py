# workers/db_saver_celery_worker.py

import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "db_saver",
    broker=os.getenv("BROKER_URL"),  # e.g. redis://localhost:6379/0
    backend=os.getenv("RESULT_BACKEND_URL", os.getenv("BROKER_URL")),
)

# tell Celery “look under the app package for tasks”
celery_app.autodiscover_tasks(packages=["workers"])
