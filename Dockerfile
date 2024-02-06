FROM python:3.11.2-alpine

EXPOSE 8081

WORKDIR /app

RUN pip install --upgrade pip && apk add gcc musl-dev libffi-dev && pip install poetry 

COPY . /app

# virtual env is created in "/app/.venv" directory
ENV POETRY_NO_INTERACTION=1 \
POETRY_VIRTUALENVS_IN_PROJECT=1 \
POETRY_VIRTUALENVS_CREATE=true \
POETRY_CACHE_DIR=/tmp/poetry_cache
# Install dependencies
RUN --mount=type=cache,target=/tmp/poetry_cache poetry install --only main --no-root
RUN poetry install

CMD ["poetry","run","uvicorn","fastapi_auth.server:create_app","--host","0.0.0.0","--port","8081"]
