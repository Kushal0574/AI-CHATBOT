from chatbot.bot import ChatBot

def main():
    print("🤖 AI Chatbot (OpenAI-powered) started. Type 'exit' to quit.\n")
    bot = ChatBot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break

        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
