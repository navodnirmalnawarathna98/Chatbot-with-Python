# Gemini AI Chatbot with Python

A beginner-friendly terminal chatbot built with **Python**, **Google
Gemini API**, and the official **Google Gen AI Python SDK**.

This repository explains the project from A to Z: the idea,
architecture, folder structure, Python commands, dependencies, API
integration, chat sessions, troubleshooting, and exercises.

> **Project status:** Beginner terminal chatbot\
> **Platform:** Windows / PowerShell / VS Code\
> **Language:** Python\
> **AI provider:** Google Gemini Developer API

------------------------------------------------------------------------

## Table of Contents

1.  [Project Overview](#1-project-overview)
2.  [How the Chatbot Works](#2-how-the-chatbot-works)
3.  [Technologies Used](#3-technologies-used)
4.  [Project Structure](#4-project-structure)
5.  [Prerequisites](#5-prerequisites)
6.  [Get a Gemini API Key](#6-get-a-gemini-api-key)
7.  [Set Up the Project](#7-set-up-the-project)
8.  [Understand the Terminal
    Commands](#8-understand-the-terminal-commands)
9.  [Configure the Project Files](#9-configure-the-project-files)
10. [Complete Python Source Code](#10-complete-python-source-code)
11. [Run the Chatbot](#11-run-the-chatbot)
12. [Understand the Python Code](#12-understand-the-python-code)
13. [Understand Chat Memory](#13-understand-chat-memory)
14. [Customize the Chatbot's
    Personality](#14-customize-the-chatbots-personality)
15. [List Available Gemini Models](#15-list-available-gemini-models)
16. [Troubleshooting](#16-troubleshooting)
17. [Security and Free-Tier Notes](#17-security-and-free-tier-notes)
18. [Practice Exercises](#18-practice-exercises)
19. [Future Improvements](#19-future-improvements)
20. [Useful Resources](#20-useful-resources)

------------------------------------------------------------------------

## 1. Project Overview

A chatbot is a software application that allows a person to communicate
with a computer using messages.

A traditional rule-based chatbot responds to predefined conditions. For
example:

``` python
message = input("You: ")

if message.lower() == "hello":
    print("Bot: Hello!")

else:
    print("Bot: I do not understand.")
```

This approach only handles cases that the developer has programmed.

This project uses **Generative AI**. Instead of writing a response for
every possible question, the Python application sends the user's message
to a Gemini model. Gemini generates a response and sends it back to the
application.

### Project objectives

By completing this project, you will learn how to:

-   Create and activate a Python virtual environment.
-   Install and manage Python packages.
-   Store API credentials in an environment file.
-   Connect a Python application to Google's Gemini API.
-   Create a multi-turn chat session.
-   Receive and display AI-generated responses.
-   Use Python functions, loops, conditions, and exception handling.
-   Reset a conversation and handle basic chatbot commands.

------------------------------------------------------------------------

## 2. How the Chatbot Works

### 2.1 What is Generative AI?

Generative AI is a type of artificial intelligence that can generate new
content, such as text, code, summaries, explanations, and translations,
based on input.

### 2.2 What is Google Gemini?

Google Gemini is Google's family of generative AI models. We use a
Gemini model through Google's API rather than installing or training the
model on our computer.

### 2.3 What is an API?

API means **Application Programming Interface**. It provides a way for
separate software applications to communicate.

In this project:

-   The Python chatbot is the application making a request.
-   The Gemini API is the communication interface.
-   The Gemini model processes the prompt and generates a response.
-   The Python application displays the returned text.

### 2.4 Request and response flow

``` text
+----------------------+
|         USER         |
| Types a question     |
+----------+-----------+
           |
           v
+----------------------+
|   PYTHON APPLICATION |
| Reads the user input |
+----------+-----------+
           |
           v
+----------------------+
|     GOOGLE GEN AI    |
|      PYTHON SDK      |
| Prepares API request |
+----------+-----------+
           |
           v
+----------------------+
|     GEMINI API       |
| Authenticates request|
+----------+-----------+
           |
           v
+----------------------+
|     GEMINI MODEL     |
| Generates an answer  |
+----------+-----------+
           |
           v
+----------------------+
|    API RESPONSE      |
| Returns generated text|
+----------+-----------+
           |
           v
+----------------------+
|   PYTHON APPLICATION |
| Displays the answer  |
+----------------------+
```

**Important:** The Gemini model runs on Google's infrastructure. It is
not installed inside the project's `.venv` folder. The Python
application communicates with Google over the internet.

------------------------------------------------------------------------

## 3. Technologies Used

  Technology          Purpose
  ------------------- ------------------------------------------------
  Python              Main programming language
  Google Gemini API   Generates AI responses
  `google-genai`      Official Google Gen AI Python SDK
  `python-dotenv`     Loads values from the `.env` file
  `.env`              Stores local configuration such as the API key
  `venv`              Creates an isolated Python environment
  VS Code             Code editor
  PowerShell          Windows command-line shell

### What is a Python SDK?

SDK means **Software Development Kit**. The Google Gen AI SDK provides
Python methods for communicating with Google's generative AI services.
It handles much of the request formatting and API communication.

### What is a virtual environment?

A virtual environment is an isolated Python environment for a project.
It helps prevent package versions in one project from interfering with
another project.

------------------------------------------------------------------------

## 4. Project Structure

After setup, the project should look like this:

``` text
gemini_chat_bot/
│
├── .venv/
│   ├── Scripts/
│   └── Lib/
│
├── main.py
├── check_models.py
├── .env
├── .gitignore
└── requirements.txt
```

  -----------------------------------------------------------------------
  File or folder                      Purpose
  ----------------------------------- -----------------------------------
  `.venv/`                            Isolated Python interpreter and
                                      installed packages

  `main.py`                           Main chatbot application

  `check_models.py`                   Optional utility to list models
                                      available to the API key

  `.env`                              Stores the Gemini API key locally

  `.gitignore`                        Tells Git which files and folders
                                      to ignore

  `requirements.txt`                  Lists project dependencies
  -----------------------------------------------------------------------

### Why use separate files?

-   **`main.py`:** Keeps the application logic in one clear entry-point
    file.
-   **`.env`:** Separates secret configuration from source code. It is
    not encrypted; protect access to it.
-   **`requirements.txt`:** Makes it easier for another developer to
    install the project's dependencies.
-   **`.gitignore`:** Helps prevent secrets, virtual environments, and
    temporary files from being committed.
-   **`.venv/`:** Keeps this project's installed packages separate from
    other Python projects.

You normally do not edit files inside `.venv/` manually.

------------------------------------------------------------------------

## 5. Prerequisites

Install the following before starting:

1.  Python 3.10 or a newer version supported by the installed Google Gen
    AI SDK.
2.  Visual Studio Code.
3.  Internet connection.
4.  A Google account.
5.  A Gemini API key from Google AI Studio.

Check your Python installation:

``` powershell
python --version
```

Check that Python is available:

``` powershell
python -c "import sys; print(sys.executable)"
```

If `python` is not recognized, install Python and ensure it is available
in PATH, or use the Python launcher (`py`) if installed.

------------------------------------------------------------------------

## 6. Get a Gemini API Key

1.  Open [Google AI Studio -- API
    keys](https://aistudio.google.com/apikey).
2.  Sign in with your Google account.
3.  Create an API key.
4.  Copy the key and keep it private.

The key is used to authenticate your application when it calls the
Gemini API.

**Never:**

-   Publish your API key in a public GitHub repository.
-   Share it in screenshots, messages, or public documentation.
-   Hard-code it into `main.py`.
-   Commit the `.env` file.

------------------------------------------------------------------------

## 7. Set Up the Project

### Step 1: Create a project folder

For example:

``` text
C:\Users\NOVA\Desktop\gemini_chat_bot
```

Open this folder in VS Code.

### Step 2: Open the terminal

In VS Code, select:

**Terminal → New Terminal**

PowerShell should show a prompt similar to:

``` powershell
PS C:\Users\NOVA\Desktop\gemini_chat_bot>
```

### Step 3: Create a virtual environment

Run this once if `.venv` does not already exist:

``` powershell
python -m venv .venv
```

This runs Python's built-in `venv` module and creates the `.venv`
directory.

Do not recreate the environment if it already exists and works.

### Step 4: Activate the virtual environment

For PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the prompt should start with:

``` powershell
(.venv) PS C:\Users\NOVA\Desktop\gemini_chat_bot>
```

The `(.venv)` prefix indicates that the virtual environment is active in
this terminal.

If PowerShell blocks activation, run the following for the current
terminal session:

``` powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

``` powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Upgrade pip

``` powershell
python -m pip install --upgrade pip
```

`pip` is Python's package installer. The `python -m pip` form runs pip
using the currently selected Python interpreter, which helps avoid
accidentally using a different global Python installation.

### Step 6: Install the dependencies

``` powershell
python -m pip install google-genai python-dotenv
```

This installs:

-   `google-genai`: Google's official Python SDK.
-   `python-dotenv`: Loads variables from `.env`.

### Step 7: Verify the packages

``` powershell
python -m pip show google-genai
```

``` powershell
python -m pip show python-dotenv
```

You can also list all installed packages:

``` powershell
python -m pip list
```

Check the package `Location` shown by `pip show`. It should point inside
your project's `.venv` directory.

------------------------------------------------------------------------

## 8. Understand the Terminal Commands

  ---------------------------------------------------------------------------------
  Command                                       Explanation
  --------------------------------------------- -----------------------------------
  `python --version`                            Displays the Python version

  `python -m venv .venv`                        Creates a virtual environment

  `.\.venv\Scripts\Activate.ps1`                Activates the environment in
                                                PowerShell

  `deactivate`                                  Deactivates the active environment

  `python -m pip --version`                     Displays pip version and location

  `python -m pip install PACKAGE`               Installs a package

  `python -m pip list`                          Lists installed packages

  `python -m pip show PACKAGE`                  Displays package details

  `python -m pip install -r requirements.txt`   Installs dependencies listed in a
                                                file

  `python main.py`                              Runs the chatbot

  `python check_models.py`                      Lists available model identifiers
  ---------------------------------------------------------------------------------

### Why did `pip install` fail previously?

A Windows pip launcher can refer to a Python installation that has been
removed or moved. In this project, the old global `pip.exe` pointed to a
missing Python 3.8 executable.

Using the activated environment and this command fixed the issue:

``` powershell
python -m pip install google-genai python-dotenv
```

This invokes pip through the active Python interpreter.

### Why did the `/c:/.../python.exe` command fail?

That is not the normal Windows PowerShell executable path format. In
PowerShell, use:

``` powershell
.\.venv\Scripts\python.exe -m pip install google-genai python-dotenv
```

Or, after activation, simply use:

``` powershell
python -m pip install google-genai python-dotenv
```

------------------------------------------------------------------------

## 9. Configure the Project Files

### 9.1 `requirements.txt`

Create a file named `requirements.txt`:

``` text
google-genai
python-dotenv
```

This file records the direct dependencies. To install them later in a
fresh environment:

``` powershell
python -m pip install -r requirements.txt
```

For a reproducible deployment, consider pinning tested dependency
versions after validating the project.

### 9.2 `.env`

Create a file named exactly `.env` in the project root:

``` env
GEMINI_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

Replace the placeholder with your real key. Do not add quotes unless the
value requires them.

### 9.3 `.gitignore`

Create `.gitignore`:

``` gitignore
# Virtual environment
.venv/

# Environment variables and secrets
.env

# Python cache files
__pycache__/
*.py[cod]

# Editor and operating system files
.vscode/
.DS_Store
Thumbs.db
```

The `.env` file must remain local and must not be committed to Git.

------------------------------------------------------------------------

## 10. Complete Python Source Code

Create `main.py` in the project root.

The program below includes:

-   API key loading and validation.
-   Gemini client creation.
-   Chat session creation.
-   Welcome and help messages.
-   User input validation.
-   Sending messages to Gemini.
-   Conversation reset.
-   Error handling.
-   Client cleanup.

``` python
# ==========================================================
# PROJECT: GEMINI AI CHATBOT
# LANGUAGE: PYTHON
# AI PROVIDER: GOOGLE GEMINI
# ==========================================================


# ----------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ----------------------------------------------------------

import os

from dotenv import load_dotenv
from google import genai


# ----------------------------------------------------------
# 2. LOAD ENVIRONMENT VARIABLES
# ----------------------------------------------------------

# Read values from the .env file.
load_dotenv()

# Retrieve the Gemini API key.
API_KEY = os.getenv("GEMINI_API_KEY")


# Stop if the API key is missing.
if not API_KEY:
    raise SystemExit(
        "Gemini API key not found. "
        "Please check the .env file."
    )


# ----------------------------------------------------------
# 3. CONFIGURE THE MODEL
# ----------------------------------------------------------

# This model ID is used in the example.
# If it is unavailable to your account, use a supported
# text-generation model listed by check_models.py.
MODEL_NAME = "gemini-3.8-flash"


# ----------------------------------------------------------
# 4. CREATE THE GEMINI CLIENT
# ----------------------------------------------------------

client = genai.Client(
    api_key=API_KEY
)


# ----------------------------------------------------------
# 5. CREATE A CHAT SESSION
# ----------------------------------------------------------

chat = client.chats.create(
    model=MODEL_NAME
)


# ----------------------------------------------------------
# 6. DISPLAY THE WELCOME MESSAGE
# ----------------------------------------------------------

def display_welcome():

    print("\n")
    print("=" * 60)

    print("              GEMINI AI CHATBOT")

    print("=" * 60)

    print("Welcome! I am your AI assistant.")
    print("You can ask me questions about anything.")

    print("-" * 60)

    print("Commands:")
    print("exit  - Close chatbot")
    print("clear - Start a new conversation")
    print("help  - Display available commands")

    print("=" * 60)


# ----------------------------------------------------------
# 7. DISPLAY HELP INFORMATION
# ----------------------------------------------------------

def display_help():

    print("\nAvailable commands:")

    print("1. exit  - Exit chatbot")
    print("2. clear - Reset conversation")
    print("3. help  - Show help information")


# ----------------------------------------------------------
# 8. CREATE A NEW CHAT SESSION
# ----------------------------------------------------------

def create_new_chat():

    global chat

    chat = client.chats.create(
        model=MODEL_NAME
    )

    print("\nGemini: New conversation started!")


# ----------------------------------------------------------
# 9. SEND A MESSAGE TO GEMINI
# ----------------------------------------------------------

def send_message(user_message):

    try:

        print("\nGemini is thinking...")

        # Send the user's message to Gemini.
        response = chat.send_message(
            message=user_message
        )

        # Retrieve the generated text.
        answer = response.text

        if answer:

            print("\nGemini:")
            print(answer)

        else:

            print("\nGemini did not return text.")

    except Exception as error:

        print("\nUnable to communicate with Gemini.")
        print("Error:", error)


# ----------------------------------------------------------
# 10. MAIN CHATBOT FUNCTION
# ----------------------------------------------------------

def start_chatbot():

    display_welcome()

    while True:

        try:

            # Read the user's message.
            user_message = input("\nYou: ").strip()

            # Validate empty messages.
            if not user_message:

                print("Please enter a message.")
                continue

            # Exit command.
            if user_message.lower() == "exit":

                print("\nGemini: Goodbye! Have a nice day.")
                break

            # Clear command.
            elif user_message.lower() == "clear":

                create_new_chat()
                continue

            # Help command.
            elif user_message.lower() == "help":

                display_help()
                continue

            # Send normal messages to Gemini.
            else:

                send_message(user_message)

        except KeyboardInterrupt:

            print("\n\nChatbot interrupted by user.")
            break


# ----------------------------------------------------------
# 11. APPLICATION ENTRY POINT
# ----------------------------------------------------------

if __name__ == "__main__":

    try:

        start_chatbot()

    finally:

        # Close the Gemini client.
        client.close()

        print("\nApplication closed successfully.")
```

------------------------------------------------------------------------

## 11. Run the Chatbot

Make sure the terminal is inside the project directory and the virtual
environment is activated.

### Step 1: Activate the environment

``` powershell
.\.venv\Scripts\Activate.ps1
```

### Step 2: Run the program

``` powershell
python main.py
```

### Step 3: Test the chatbot

Example conversation:

``` text
============================================================
              GEMINI AI CHATBOT
============================================================
Welcome! I am your AI assistant.
You can ask me questions about anything.
------------------------------------------------------------
Commands:
exit  - Close chatbot
clear - Start a new conversation
help  - Display available commands
============================================================

You: What is Python?

Gemini is thinking...

Gemini:
Python is a high-level programming language used for
web development, automation, data science and AI.

You: Explain OOP with a simple example.

Gemini is thinking...

Gemini:
Object-Oriented Programming is a programming approach
based on objects and classes...

You: clear

Gemini: New conversation started!

You: exit

Gemini: Goodbye! Have a nice day.

Application closed successfully.
```

The actual responses will be generated by Gemini and may differ from
this example.

------------------------------------------------------------------------

## 12. Understand the Python Code

### 12.1 Import statements

``` python
import os

from dotenv import load_dotenv
from google import genai
```

`import` allows us to use functionality provided by Python modules and
installed packages.

-   `os`: A built-in Python module for operating-system functionality,
    including environment variables.
-   `load_dotenv`: Loads variables from the `.env` file.
-   `genai`: Provides the Google Gen AI SDK.

### 12.2 Load the API key

``` python
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
```

`load_dotenv()` reads the `.env` file and makes its values available as
environment variables.

`os.getenv()` retrieves the value associated with the specified variable
name.

### 12.3 Validate the API key

``` python
if not API_KEY:
    raise SystemExit("Gemini API key not found.")
```

This checks whether the key exists. If it does not, the application
stops rather than continuing with invalid configuration.

### 12.4 Configure the model

``` python
MODEL_NAME = "gemini-3.8-flash"
```

This variable stores the model identifier. Keeping it in one place makes
it easier to change the model later.

### 12.5 Create the client

``` python
client = genai.Client(
    api_key=API_KEY
)
```

This creates the SDK client used to communicate with the Gemini
Developer API.

### 12.6 Create a chat session

``` python
chat = client.chats.create(
    model=MODEL_NAME
)
```

This creates a multi-turn chat session. Subsequent messages sent through
the same chat can use earlier conversation context.

### 12.7 Functions

A function is a reusable block of code.

For example:

``` python
def display_welcome():
    print("Welcome to Gemini AI Chatbot!")
```

Call it using:

``` python
display_welcome()
```

In this project:

  Function              Responsibility
  --------------------- -------------------------------------------
  `display_welcome()`   Displays the welcome message
  `display_help()`      Displays available commands
  `create_new_chat()`   Creates a fresh conversation
  `send_message()`      Sends a message and displays the response
  `start_chatbot()`     Runs the main conversation loop

### 12.8 The `while` loop

``` python
while True:
    user_message = input("You: ")
```

The loop keeps accepting messages until a `break` statement stops it.

### 12.9 User input

``` python
user_message = input("\nYou: ").strip()
```

`input()` reads text entered by the user. `.strip()` removes leading and
trailing whitespace.

### 12.10 Conditions

``` python
if user_message.lower() == "exit":
    break
```

The `if` statement checks a condition. `.lower()` makes the comparison
case-insensitive.

For example, `EXIT`, `Exit`, and `exit` are treated the same.

### 12.11 Send a message

``` python
response = chat.send_message(
    message=user_message
)
```

This sends the user's message through the SDK to the Gemini API.

The SDK handles the underlying API request and response communication.

### 12.12 Read the response

``` python
answer = response.text
print(answer)
```

The response object contains the generated content. `.text` retrieves
its text representation.

### 12.13 Exception handling

``` python
try:
    response = chat.send_message(
        message=user_message
    )

except Exception as error:
    print("Error:", error)
```

The `try` block contains code that might fail. The `except` block
handles an exception so that the application can display an error
instead of unexpectedly terminating.

### 12.14 Application entry point

``` python
if __name__ == "__main__":
    start_chatbot()
```

This is a common Python convention. It runs the chatbot when the file is
executed directly, but does not automatically start it if the file is
imported by another Python module.

------------------------------------------------------------------------

## 13. Understand Chat Memory

### 13.1 What is conversation memory?

Conversation memory is the ability to use earlier messages as context
for later messages.

For example:

``` text
User: My name is Alex.

Gemini: Nice to meet you, Alex!

User: What is my name?

Gemini: Your name is Alex.
```

The second question can be answered because the earlier conversation is
included in the chat context.

### 13.2 Session-based memory

Our application uses:

``` python
chat = client.chats.create(
    model=MODEL_NAME
)
```

Messages are sent through the same chat object:

``` python
chat.send_message("My name is Alex.")

chat.send_message("What is my name?")
```

The SDK manages the conversation history for the session.

### 13.3 Does this save conversations permanently?

No. The current terminal program does not save chat history to a local
database.

When the program closes, its in-memory chat object is lost.

### 13.4 How can we save conversations permanently?

A database such as SQLite can store:

-   Conversation IDs.
-   User messages.
-   AI responses.
-   Timestamps.

Example database table:

  -----------------------------------------------------------------------
  ID                User message      AI response       Date
  ----------------- ----------------- ----------------- -----------------
  1                 What is Python?   Python is a       Example date
                                      programming       
                                      language.         

  2                 Explain OOP       OOP is a          Example date
                                      programming       
                                      paradigm.         
  -----------------------------------------------------------------------

A database alone does not give the model memory. The application must
retrieve relevant previous messages and provide them to the model as
context when needed.

------------------------------------------------------------------------

## 14. Customize the Chatbot's Personality

A system instruction provides behavioural guidance to the model.

For example, we can make the chatbot act as a Python programming tutor.

Add this import:

``` python
from google.genai import types
```

Replace the existing chat creation section with:

``` python
chat = client.chats.create(

    model=MODEL_NAME,

    config=types.GenerateContentConfig(

        system_instruction="""
        You are a friendly Python programming tutor.

        Your responsibilities:

        1. Explain concepts using simple English.
        2. Provide beginner-friendly examples.
        3. Explain code step by step.
        4. Encourage students to practise.
        5. Give short exercises when appropriate.

        Always be helpful and professional.
        """
    )
)
```

Now the model receives the system instruction as part of the chat
configuration.

You can change the instruction to create:

-   An English language learning assistant.
-   A university student support chatbot.
-   A Python programming tutor.
-   A customer support assistant.

------------------------------------------------------------------------

## 15. List Available Gemini Models

Model availability can vary by API, account, and time. If a model
returns a `404 NOT_FOUND` error, check the model identifiers available
to your API key.

Create `check_models.py`:

``` python
import os

from dotenv import load_dotenv
from google import genai


# Load API key
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise SystemExit("Gemini API key not found.")


# Connect to Gemini
client = genai.Client(
    api_key=API_KEY
)


print("\nAVAILABLE GEMINI MODELS")
print("=" * 50)

try:

    models = client.models.list()

    for model in models:

        print(model.name)

except Exception as error:

    print("Unable to retrieve models:", error)

finally:

    client.close()
```

Run:

``` powershell
python check_models.py
```

Choose a model that supports text generation and is available to your
account. Update `MODEL_NAME` in `main.py` if required.

------------------------------------------------------------------------

## 16. Troubleshooting

  ----------------------------------------------------------------------------
  Error                        Possible reason         Suggested solution
  ---------------------------- ----------------------- -----------------------
  `ModuleNotFoundError`        Required package is not Activate `.venv` and
                               installed in the active install dependencies
                               environment             

  `GEMINI_API_KEY not found`   Missing or incorrectly  Check the file name,
                               named `.env` file       location, and variable

  `API_KEY_INVALID`            Incorrect or revoked    Create or verify an API
                               key                     key

  `404 NOT_FOUND`              Model ID is invalid or  List available models
                               unavailable             and choose a supported
                                                       one

  `429 RESOURCE_EXHAUSTED`     Rate or usage limit     Check usage and retry
                               reached                 after the limit resets

  Connection error             Internet or network     Check internet access
                               issue                   

  `python not recognized`      Python is not available Check Python
                               in PATH                 installation or use the
                                                       active environment

  pip launcher error           Global pip points to a  Activate `.venv` and
                               missing Python          use `python -m pip`
                               installation            
  ----------------------------------------------------------------------------

### Check which Python interpreter is active

``` powershell
python -c "import sys; print(sys.executable)"
```

Expected output should point to:

``` text
...\gemini_chat_bot\.venv\Scripts\python.exe
```

### Check whether the API key is loaded

You can temporarily add this to `main.py`:

``` python
print("API key loaded:", bool(API_KEY))
```

This displays `True` or `False` without exposing the actual key.

Never print the actual API key.

------------------------------------------------------------------------

## 17. Security and Free-Tier Notes

### API key security

-   Keep `.env` out of Git.
-   Do not expose your API key in public screenshots or source code.
-   If a key is accidentally published, revoke it and create a
    replacement.
-   For a deployed application, store the key in the hosting provider's
    secret/environment configuration.
-   Never put the Gemini API key in frontend JavaScript.

### Free-tier usage

Google offers free-tier access for eligible Gemini API models, subject
to usage limits and account eligibility.

Limits may include requests per minute, tokens per minute, and requests
per day. They can change over time.

Review the latest details:

-   [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
-   [Google AI Studio](https://aistudio.google.com/)
-   [Gemini API documentation](https://ai.google.dev/gemini-api/docs)

Review Google's data-use terms before sending sensitive information.
Avoid sending confidential student, personal, or institutional
information to an API unless the relevant data-handling requirements
have been checked.

------------------------------------------------------------------------

## 18. Practice Exercises

Complete these exercises to improve your Python and AI integration
skills.

1.  Change the chatbot name to `Python Learning Assistant`.
2.  Ask Gemini to explain a programming topic in Sinhala.
3.  Add a `time` command to display the current date and time.
4.  Add a `count` command to count user messages.
5.  Validate the maximum length of a user message.
6.  Save chat history to a local text file.
7.  Add a system instruction that makes Gemini act as a university
    lecturer.
8.  Display a friendly message when the user enters an unknown command.
9.  Add a confirmation before clearing a conversation.
10. Experiment with different supported Gemini models.

------------------------------------------------------------------------

## 19. Future Improvements

This repository is the first stage of a larger AI chatbot application.

Possible next stages:

### Stage 1 -- Terminal chatbot (current project)

-   Python fundamentals.
-   Gemini API integration.
-   Chat sessions.
-   Basic error handling.

### Stage 2 -- Web-based chatbot

Suggested technologies:

-   Python Flask backend.
-   HTML, CSS, and JavaScript frontend.
-   Bootstrap 5 for responsive UI.
-   Gemini API integration.
-   Chat interface and loading indicators.

### Stage 3 -- Database integration

-   SQLite database.
-   User registration and login.
-   Persistent conversation history.
-   Multiple chat sessions.

### Stage 4 -- Advanced AI features

-   PDF document uploads.
-   Document question answering.
-   Retrieval-Augmented Generation (RAG).
-   Voice input and output.
-   Knowledge-base integration.

------------------------------------------------------------------------

## 20. Useful Resources

  ----------------------------------------------------------------------------------------------------------
  Resource                                                               Purpose
  ---------------------------------------------------------------------- -----------------------------------
  [Python Documentation](https://docs.python.org/3/)                     Python language reference

  [Google Gen AI Python SDK](https://googleapis.github.io/python-genai/) SDK installation and usage

  [Google Gen AI SDK on                                                  SDK source and examples
  GitHub](https://github.com/googleapis/python-genai)                    

  [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)      API concepts and features

  [Gemini Models](https://ai.google.dev/gemini-api/docs/models)          Model names and capabilities

  [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)    Usage and pricing information

  [Google AI Studio](https://aistudio.google.com/)                       Create and manage API keys

  [Python dotenv](https://pypi.org/project/python-dotenv/)               Environment variable package

  [VS Code Python                                                        Python development in VS Code
  Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)   
  ----------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## License

This project is intended as a beginner-friendly educational
demonstration. Add a license file to the repository if you intend to
distribute or reuse the project under specific terms.

------------------------------------------------------------------------

## Author

**Gemini AI Chatbot -- Python Practical Project**

Built to learn Python programming, API integration, and Generative AI
fundamentals.

If you find this project useful, consider starring the repository on
GitHub.
