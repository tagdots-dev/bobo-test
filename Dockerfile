# Use the official AWS Lambda Python base image
FROM python:3.12-slim

# Install uv inside the image container
COPY --from=ghcr.io/astral-sh/uv:0.12 /uv /uvx /bin/

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

# Copy configuration files
COPY pyproject.toml uv.lock README.md ./

# Copy application code
COPY src/ ./src/
COPY config/ ./config/

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app

# Switch to appuser
USER appuser

# Install dependencies and project package
RUN uv sync --frozen --no-default-groups --python-preference=only-system

# Run the application
CMD ["pkg-40400"]
