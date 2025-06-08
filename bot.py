# sujal_chatbot.py

# Dictionary of simple responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Need any assistance?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm SujalBot, your friendly assistant!",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I don't understand that."
}

# Function to get response from the dictionary
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

# Main chat loop
def chat():
    print("🤖 Welcome to SujalBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot:", responses["bye"])
            break
        response = get_response(user_input)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
