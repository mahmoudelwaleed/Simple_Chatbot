import streamlit as st
import requests
import uuid


# Initialize Backend URL
Backend_url = 'http://backend:9999/chat/'

# Initialize user_id and chat history
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if 'messages' not in st.session_state:
    st.session_state.messages = []

# make title
st.title('ChatBot')

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'*{message["role"]}* : {message["message"]}')


# Define User input
user_input = st.chat_input('Enter your message...')

# Check is user input submitted
if user_input:

    # append user_message to session_state
    st.session_state.messages.append({ 'role' : 'User' , 'message' : user_input})

    # Display user message
    with st.chat_message("User"):
        st.markdown(f'*User* : {user_input}')

    # send request to fastapi
    with st.spinner('Thinking...'):
        response = requests.post(
            Backend_url,
            json = {'user_id' : st.session_state.user_id , 'message' : user_input}
        )
        print(response)

    # check if there is response
    if response.status_code == 200:
        bot_reply = response.json()['response']

    else:
        bot_reply = 'I can\'t reach to chatbot backend'

    # append response to stession_state
    st.session_state.messages.append({'role' : 'Assistant' , 'message' : bot_reply})

    # Display Bot response
    with st.chat_message("Assistant"):
        st.markdown(f'*Bot* : {bot_reply}')


