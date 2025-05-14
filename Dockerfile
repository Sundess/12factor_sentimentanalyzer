# Dockerfile
FROM python:3.10-slim

# set a working dir
WORKDIR /app

# install OS dependencies if you need any (e.g. libpq-dev for Postgres client)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy in your code
COPY . .

# by default, run uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
