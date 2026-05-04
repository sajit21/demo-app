FROM python:3.11-alpine

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn

# Copy application code
COPY . .

# Fix ownership so non-root user can run it
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose port (documentation only)
EXPOSE 5000

# Run production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
