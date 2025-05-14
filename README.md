# 12factor_sentimetAnalyzer

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Sentiment Analyzer API is a FastAPI application designed for sentiment analysis, powered by Groq’s LLaMA 4 model. It efficiently processes input text to determine sentiment using advanced natural language understanding. The application integrates Celery for asynchronous background task processing and PostgreSQL for reliable data storage. Docker is utilized to streamline deployment and ensure a consistent, containerized environment.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         12factor_sentimetanalyzer and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── 12factor_sentimetanalyzer   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes 12factor_sentimetanalyzer a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

---

## Running with Docker

This project provides a Docker setup for easy development and deployment. The application runs on Python 3.10 (slim) and uses a multi-stage build for efficient image size and dependency management.

### Requirements

- Docker and Docker Compose installed on your system.
- A `.env` file for environment variables. Change the `.env_change` file (insert your groq key)

### Build and Run

To build and start the application using Docker Compose:

```
docker compose up --build
```

This will:

- Build the Docker image using the provided `Dockerfile` (Python 3.10-slim base)
- Install all dependencies from `requirements.txt` and `pyproject.toml` in a virtual environment
- Start the FastAPI app with Uvicorn

### Configuration

- The application runs as a non-root user (`appuser`) inside the container.
- No external services (e.g., databases) are required by default.
- If you need to set environment variables, create a `.env` file in the project root and uncomment the `env_file` line in `docker-compose.yml`.

### Ports

- The FastAPI app is exposed on port **8000**. The service is mapped to `localhost:8000` on your machine.

### Example

After running `docker compose up --build`, access the API at:

```
http://localhost:8000
```

If you add additional services (e.g., a database), update `docker-compose.yml` accordingly.
