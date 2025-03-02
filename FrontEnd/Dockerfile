FROM python:3.8-slim
WORKDIR /Frontend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "Frontend.py", "--server.address=0.0.0.0", "--server.port=8501"]