import cohere

co = cohere.Client("")

def chat_with_cohere(prompt):
    response = co.chat(message=prompt)
    return response.text

user_input = "hi"
print(chat_with_cohere(user_input))