FROM python:3.11-alpine

RUN addgroup -S appgroup && adduser -S -u 10001 appuser -G appgroup

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn

COPY . .

RUN chown -R 10001:appgroup /app

USER 10001

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
