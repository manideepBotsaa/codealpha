def chatbot():
    print("🤖 Chatbot: Hello my name is siri! Type something to start a conversation. (type 'bye' to exit)")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine Hope you are doing well, thanks!")
        elif user_input == "can you help me":
            print("🤖 Chatbot: yaa, ask me i am ready to help you!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye,have a nice day!")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()

