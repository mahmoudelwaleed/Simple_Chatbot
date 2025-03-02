# Containerized End-to-End LLM Application

This project implements a simple chatbot using Cohere's LLM API with a FastAPI backend and Streamlit frontend, all containerized with Docker for easy deployment.

## Project Structure

├── BackEnd/
│   ├── Backend.py       # FastAPI application that connects to Cohere's API
│   ├── Dockerfile       # Docker configuration for backend
│   ├── requirements.txt # Python dependencies for backend
│   └── .env             # Environment variables (API keys)
├── FrontEnd/
│   ├── Frontend.py      # Streamlit UI for chatbot interaction
│   ├── Dockerfile       # Docker configuration for frontend
│   └── requirements.txt # Python dependencies for frontend
├── docker-compose.yml   # Docker Compose configuration for orchestration
└── README.md            # Project documentation


## Features
- *Backend API:* FastAPI service handling user queries and communicating with Cohere's LLM API
- *Frontend UI:* Streamlit interface allowing users to interact with the chatbot
- *Conversation History:* Maintains chat history for context
- *Docker Integration:* Containerized for consistent deployment across environments

## Prerequisites
- Docker and Docker Compose installed
- Cohere API key (sign up at [cohere.ai](https://cohere.ai))

## Setup Instructions

### Clone the repository:
bash
git clone https://github.com/yourusername/containerized-llm-app.git
cd containerized-llm-app


### Create a .env file in the BackEnd directory with your Cohere API key:
env
COHERE_API_KEY=your_cohere_api_key_here


### Build and run the containers:
bash
docker-compose up -d


## Access the application:
- *Frontend:* [http://localhost:8501](http://localhost:8501)
- *Backend API:* [http://localhost:9999](http://localhost:9999)

## Usage
1. Open your browser and navigate to [http://localhost:8501](http://localhost:8501)
2. Enter your query in the text input field
3. The application will process your query through the LLM and display the response
4. Your conversation history will be displayed in the chat interface

## API Endpoints
### *POST* /chat/ - Send a message to the chatbot
#### *Request body:*
json
{
  "user_id": "string",
  "message": "string"
}

#### *Response:*
```json
{
  "response": "string"
}
