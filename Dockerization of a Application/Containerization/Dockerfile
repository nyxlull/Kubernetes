# ---------- Stage 1: Build environment ----------
FROM python:3.11-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Stage 2: Final image ----------
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app/ ./app

EXPOSE 5000

CMD ["python", "app/main.py"]
