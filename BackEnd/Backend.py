import os
import cohere
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Dict


# Load env variables
load_dotenv()

# Create API key
Cohere_API_Key = os.getenv('COHERE_API_KEY')

# check if there is cohere api key
if not Cohere_API_Key:
    raise ValueError('Cohere API Key Not Found')

# initialize cohere client by passing cohere api key
co = cohere.Client(Cohere_API_Key)

# initialize fastapi
api = FastAPI()


# store chat history
chat_histories: Dict[str, List[Dict[str,str]]]= {}
max_hist_keep = 15

# define schema
class Query(BaseModel):
    user_id: str
    message: str

# define endpoint
@api.post('/chat/')
def chat(query: Query):
    try:

        # define history of user's conversation
        history = chat_histories.get(query.user_id,[])

        # send user message to cohere's llm 
        response = co.chat(
            message = query.message,
            chat_history = history
        )

        # append user message and response in history 
        history.append({'role': 'User', 'message': query.message})
        history.append({'role': 'Chatbot', 'message': response.text})

        # update chat_histories to keep only last 15 messages
        chat_histories[query.user_id] = history[-max_hist_keep : ]

        return {'response' : response.text}

    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

