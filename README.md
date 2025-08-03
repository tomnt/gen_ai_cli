# GenAI CLI

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
   ```bash (or PowerShell)
   git clone https://github.com/tomnt/gen_ai_cli
   ```
2. Install the required dependencies:

- **macOS/Linux (Bash/Zsh):**

```bash (or PowerShell)
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```

- **Windows (PowerShell):**

```bash (or PowerShell)
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
```

## Setting Up Your OpenAI API Key

### How to get your OpenAI API key

1. [Sign up](https://platform.openai.com/signup) for an account or [log in](https://platform.openai.com) if you already have one.
2. Search for "API keys" in the documentation or navigate to the [API keys](https://platform.openai.com/account/api-keys) section.
3. Click on "+ Create new secret key" to create a new API key.
4. Copy the generated API key and store it securely.

### Setting your OpenAI API key as an environment

You must set your OpenAI API key as an environment variable named `OPENAI_API_KEY`.

- **macOS/Linux (Bash/Zsh):**

Open the .zshrc or .bashrc, .bash_profile file.

```bash
vim ~/.zshrc         # Zsh
vim ~/.bashrc        # Bash(.bashrc)
vim ~/.bash_profile  # Bash(.bash_profile)
```

- **Windows (PowerShell):**

```powershell
# Set your OpenAI API key as an environment variable
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your_api_key_here", "User")

# To view the current OpenAI API key environment variable:
Get-ChildItem Env: | findstr 'OPENAI_API_KEY'

# # To clear the OpenAI API key environment variable, uncomment the line below
# [System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $null, "User")
```

### Write your OpenAI API key as an environment variable on the file.

```shell
export OPENAI_API_KEY="sk-your_api_key_here"
```

# To view the current OpenAI API key environment variable:

```bash
echo $OPENAI_API_KEY
```

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

### Example

```
ChatGPT CLI (type 'exit' to quit)
You: How do I print "Hello, World!" in Python?
AI: You can use the following code:
print("Hello, World!")
```

## Notes

- The script maintains conversation context, so each message is part of an ongoing conversation.
- Make sure your API key is kept secure and not shared publicly.

## License

This project is provided for educational purposes. Please refer to the OpenAI API terms of use for more information.
