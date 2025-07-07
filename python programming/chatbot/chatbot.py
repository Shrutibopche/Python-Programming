
def chatbot():
    print("Chatbot: Hello! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # convert to lowercase for easy matching

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How can I help you?")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")

# Run the chatbot
chatbot()
