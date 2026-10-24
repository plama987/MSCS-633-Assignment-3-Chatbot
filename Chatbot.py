
"""
MSCS-633-M20: Advanced Artificial Intelligence
Hands-On Assignment 3: Simple Q&A Chatbot

Description:
A terminal-based chatbot built using Python and ChatterBot.
The bot learns from example conversations and responds to
messages entered by the user.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def create_chatbot():
    """Create the chatbot and train it with sample conversations."""

    # Initialize the chatbot with the BestMatch response adapter.
    bot = ChatBot(
        "Assignment3Bot",
        logic_adapters=[
            "chatterbot.logic.BestMatch"
        ],
        database_uri="sqlite:///chatbot_database.sqlite3"
    )

    # Define example conversations for initial training.
    conversation_data = [
        "Good morning!",
        "I am doing very well, thank you for asking.",
        "How are you doing?",
        "I am doing well. How can I help you?",
        "Hello",
        "Hello! How can I help you today?",
        "Hi",
        "Hi there! Nice to meet you.",
        "How are you?",
        "I am fine, thank you.",
        "What is your name?",
        "I am a simple Q&A chatbot created using Python and ChatterBot.",
        "What can you do?",
        "I can respond to messages using my trained conversations.",
        "What is artificial intelligence?",
        "Artificial intelligence enables computers to perform tasks that normally require human intelligence.",
        "What is machine learning?",
        "Machine learning allows computers to learn patterns from data.",
        "What is Python?",
        "Python is a popular programming language used in AI, data science, and software development.",
        "Thank you",
        "You are welcome!",
        "Goodbye",
        "Goodbye! Have a great day.",
        "You're welcome.",
        "Do you like hats?",
        "I do not wear hats, but I can certainly talk about them!",
    ]

    # Train the chatbot with the sample conversation pairs.
    trainer = ListTrainer(bot)
    trainer.train(conversation_data)

    return bot


def start_chat():
    """Run the terminal-based chatbot conversation."""

    print("=" * 55)
    print("       SIMPLE Q&A CHATBOT - ASSIGNMENT 3")
    print("=" * 55)
    print("Chatbot initialized successfully.")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    print("-" * 55)

    # Initialize and train the chatbot.
    bot = create_chatbot()

    # Continue chatting until the user enters an exit command.
    while True:
        try:
            # Read a message from the user.
            user_input = input("user: ").strip()

            # Ignore empty messages.
            if not user_input:
                print("bot: Please enter a message.")
                continue

            # Stop the conversation when an exit command is entered.
            if user_input.lower() in {"exit", "quit", "bye"}:
                print("bot: Goodbye! Have a great day.")
                break

            # Generate and display the chatbot response.
            response = bot.get_response(user_input)
            print(f"bot: {response}")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully.
            print("\nbot: Chat session ended.")
            break

        except EOFError:
            # Handle terminal input ending unexpectedly.
            print("\nbot: Goodbye!")
            break

        except Exception as error:
            # Display an error without crashing the chat loop.
            print(f"bot: An error occurred: {error}")


# Run the chatbot only when this file is executed directly.
if __name__ == "__main__":
    start_chat()
