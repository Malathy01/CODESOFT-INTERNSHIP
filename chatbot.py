import datetime

print("🤖 CODSOFT Intelligent Rule-Based Chatbot")
print("Type 'help' to see what I can do.")
print("Type 'exit' to end the chat.\n")

user_name = None

def greet():
    return "Hello! Nice to meet you 😊"

def show_help():
    return (
        "I can help you with:\n"
        "- greetings (hi, hello)\n"
        "- telling date and time\n"
        "- remembering your name\n"
        "- basic conversation\n"
    )

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot:", greet())

    elif "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        print(f"Bot: Nice to meet you, {user_name}!")

    elif "what is my name" in user_input:
        if user_name:
            print(f"Bot: Your name is {user_name}.")
        else:
            print("Bot: I don't know your name yet.")

    elif "time" in user_input:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", time_now)

    elif "date" in user_input:
        date_today = datetime.date.today()
        print("Bot: Today's date is", date_today)

    elif user_input == "help":
        print("Bot:", show_help())

    elif user_input in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! Have a great day 👋")
        break

    else:
        print("Bot: I'm still learning. Please try a different question.")
