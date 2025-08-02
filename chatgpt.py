import os
from openai import OpenAI
"""This script sets up the OpenAI API key and provides a simple command-line interface to interact with ChatGPT.
It allows users to ask questions and receive answers from the AI model."""

"""# OpenAI API Key Setup
# How to get your OpenAI API key
1. Go to https://platform.openai.com/signup
2. Sign up for an account or log in if you already have one.
3. Navigate to the API keys section:
4. Click on "API keys" in the sidebar.
5. If you don't have an API key yet, click on "Create API key".
6. Copy the generated API key and store it securely.
7. You can use this key in your applications to authenticate requests to the OpenAI API.
8. To set the API key as an environment variable, you can use the following command in your terminal or command prompt:
export OPENAI_API_KEY="sk-your_api_key_here"
# Alternatively, you can set it in your code directly:
# For Windows PowerShell, you can set it like this:
# Set your OpenAI API key as an environment variable
# [System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your_api_key_here", "User")
9. To view your API key, you can go to:
https://platform.openai.com/settings/organization/api-keys

Click "+ Create new secret key"
# and copy the key to use it in your applications.
"""

""" # OpenAI API Key Setup in PowerShell
# Set your OpenAI API key as an environment variable
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your_api_key_here", "User")

# To view the current OpenAI API key environment variable in PowerShell, you can use:
Get-ChildItem Env: | findstr 'OPENAI_API_KEY'

# To clear the OpenAI API key environment variable, uncomment the line below
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $null, "User")
"""

""" # OpenAI API Key Setup in Bash
# Set your OpenAI API key as an environment variable
# export OPENAI_API_KEY="sk-your_api_key_here"
# To view the current OpenAI API key environment variable in Bash, you can use:
# echo $OPENAI_API_KEY
# To clear the OpenAI API key environment variable, uncomment the line below
# unset OPENAI_API_KEY
"""
#
api_key_var_name = 'OPENAI_API_KEY'
if api_key_var_name in os.environ:
    api_key = os.environ[api_key_var_name]
else:
    print(f'Key,"{api_key_var_name}" not found in environment variables.')
    exit()

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

"""
This script uses the OpenAI API to interact with ChatGPT.
It allows you to ask questions and receive answers from the AI model.
"""
def set_openai_api_key(self):
    os.environ["OPENAI_API_KEY"] = api_key
    client.api_key = api_key

messages=[
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