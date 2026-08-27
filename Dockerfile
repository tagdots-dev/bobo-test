# Stage 1: Get the official uv binary
FROM ghcr.io/astral-sh/uv:latest AS uv

# Stage 2: Build the final application image using Alpine Python
FROM python:3.12-alpine

# Copy uv into the container
COPY --from=uv /uv /uvx /bin/

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_NO_CACHE=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/app/.venv/bin:$PATH" \
    PROJECT_NAME=pkg-40400

# Set working directory
WORKDIR /app

# Copy dependency specifications
COPY pyproject.toml uv.lock README.md ./

# Copy application code
COPY src/ ./src/
COPY config/ ./config/

# Create non-root user
RUN adduser -D -s /bin/bash appuser && \
    chown -R appuser:appuser /app

# Switch to appuser
USER appuser

# Install dependencies into the system environment (ideal for containers)
RUN --mount=type=cache,target=/appuser/.cache/uv uv sync --frozen --no-dev --python-preference=only-system

# Run your application
CMD ["pkg-40400"]
