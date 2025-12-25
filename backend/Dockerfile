# ---------- build stage ----------
FROM python:3.11-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# ---------- runtime stage ----------
FROM python:3.11-slim
WORKDIR /app

COPY --from=builder /install /usr/local
COPY app.py .

EXPOSE 8080

HEALTHCHECK CMD curl -f http://localhost:8080/health || exit 1

CMD ["python", "app.py"]