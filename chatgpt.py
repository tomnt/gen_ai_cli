import os
from openai import OpenAI
"""This script sets up the OpenAI API key and provides a simple command-line interface to interact with ChatGPT.
It allows users to ask questions and receive answers from the AI model."""

#
api_key_var_name = 'OPENAI_API_KEY'
if api_key_var_name in os.environ:
    api_key = os.environ[api_key_var_name]
else:
    print(f'Key,"{api_key_var_name}" not found in environment variables.')
    exit()

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
]


def ask_chatgpt(question):
    messages.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=messages,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print("ChatGPT CLI (type 'exit' to quit)")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            break
        answer = ask_chatgpt(question)
        print("AI:", answer)
# This code is a simple command-line interface to interact with OpenAI's ChatGPT.
# It allows users to ask questions and receive answers from the AI model.
