FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PROJECT_NAME=pkg-40400

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock README.md ./

# Copy application code
COPY src/ ./src/
COPY config/ ./config/

# Install the package using system pip (ensures it's in the correct location)
RUN pip install -e .

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# # Expose port
# EXPOSE 8080

# # Health check
# HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
#     CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

# Run the application using the entry point defined in pyproject.toml
CMD ["pkg-40400"]
