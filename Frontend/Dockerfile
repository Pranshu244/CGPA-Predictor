FROM python:3.13-slim

WORKDIR /app

COPY frontend_requirements.txt .
RUN pip install --no-cache-dir -r frontend_requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]