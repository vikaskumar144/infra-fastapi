FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked  --no-dev
COPY main.py metrics.py .
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8080
CMD ["uv", "run", "fastapi", "run","main.py", "--host", "0.0.0.0", "--port", "8080"]
