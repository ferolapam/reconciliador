FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app/ ./app/

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.service:app", "--host", "0.0.0.0", "--port", "8000"]
