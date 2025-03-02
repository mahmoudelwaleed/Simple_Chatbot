FROM python:3.8-slim
WORKDIR /Backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 9999
CMD ["uvicorn", "Backend:api", "--host", "0.0.0.0", "--port", "9999"]