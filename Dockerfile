FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY project files .
RUN pip install --no-cache-dir -r project files
COPY . .
RUN useradd -m appuser && chown -R appuser /app
USER appuser
CMD ["python", "main.py"]
