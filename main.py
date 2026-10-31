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
