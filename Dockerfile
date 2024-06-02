FROM python:3.9-slim

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]