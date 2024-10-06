import re  # Import regular expressions for pattern matching


def simple_chatbot():
    print("Chatbot: Hi there! I'm your chatbot. How can I assist you today?")

    # Loop for continuous conversation
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase for easier matching

        # Rule 1: Greeting responses
        if re.search(r'\b(hello|hi|hey)\b', user_input):
            print("Chatbot: Hello! How are you doing today?")

        # Rule 2: Asking the chatbot's name or identity
        elif re.search(r'\b(who are you|your name|what\'s your name)\b', user_input):
            print("Chatbot: I'm a simple chatbot programmed to chat with you!")

        # Rule 3: User asking how the chatbot is doing
        elif re.search(r'\b(how are you|how do you feel)\b', user_input):
            print("Chatbot: I don't have feelings, but I'm here and ready to chat!")

        # Rule 4: Exiting the conversation
        elif re.search(r'\b(bye|exit|goodbye)\b', user_input):
            print("Chatbot: Goodbye! Have a great day!")
            break  # Stop the chatbot if the user wants to exit

        # Rule 5: Help-related queries
        elif re.search(r'\b(help|assist|support)\b', user_input):
            print("Chatbot: Sure, I'm here to help. Please ask me any questions.")

        # Rule 6: Catch-all for unknown queries
        else:
            print("Chatbot: I didn't quite understand that. Could you please ask me in a different way?")


# Start the chatbot
simple_chatbot()

