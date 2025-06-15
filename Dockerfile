FROM python:3.11-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./

ENV UV_SYSTEM_PYTHON=1
RUN uv sync --locked --no-install-project

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=.

EXPOSE 8000

CMD ["uv", "run", "fastmcp", "run", "--transport", "sse", "--host", "0.0.0.0", "--port", "8000", "app/main.py"]