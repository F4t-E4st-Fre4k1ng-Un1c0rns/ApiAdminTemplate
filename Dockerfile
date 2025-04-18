FROM python:3.12-alpine AS base

WORKDIR /backend

# README.md needed to hatchling build
COPY pyproject.toml requirements.lock README.md .
RUN	pip install uv --no-cache
RUN	uv pip install --no-cache --system -r requirements.lock

COPY . .

FROM base AS dev
CMD ["granian", "--interface", "asgi", "src/app.py", "--reload", "--host", "0.0.0.0"]

FROM base AS prod
CMD ["granian", "--interface", "asgi", "src/app.py", "--host", "0.0.0.0"]

