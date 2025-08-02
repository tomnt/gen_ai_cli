# ChatGPT CLI

This project provides a simple command-line interface (CLI) for interacting with OpenAI's ChatGPT using the OpenAI API. It allows users to ask questions and receive answers directly from the terminal.

## Features
- Command-line interface for chatting with ChatGPT
- Supports both GPT-3.5-turbo and GPT-4 models (configurable in code)
- Maintains conversation context for more natural interactions

## Prerequisites
- Python 3.7 or higher
- An OpenAI API key ([Get your API key here](https://platform.openai.com/signup))
- The `openai` Python package

## Installation
1. Clone this repository or download the `chatgpt.py` script.
2. Install the required dependencies:
   ```bash(or PowerShell)
   pip install -r requirement.txt
   ```
## Setting Up Your OpenAI API Key
You must set your OpenAI API key as an environment variable named `OPENAI_API_KEY`.

### On Windows PowerShell:
```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your_api_key_here", "User")
```

### On Bash (Linux/macOS):
```bash
export OPENAI_API_KEY="sk-your_api_key_here"
```

Alternatively, you can set the API key directly in the code (not recommended for production).

## Usage
Run the script from your terminal:

```bash
python chatgpt.py
```

You will see a prompt:
```
ChatGPT CLI (type 'exit' to quit)
You: 
```
Type your question and press Enter. The AI will respond. Type `exit` or `quit` to end the session.

## Notes
- The script maintains conversation context, so each message is part of an ongoing conversation.
- Make sure your API key is kept secure and not shared publicly.

## License
This project is provided for educational purposes. Please refer to the OpenAI API terms of use for more information.
