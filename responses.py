def get_fallback_response(intent: str) -> str:
    if intent == "greeting":
        return "Hello! How can I help you today?"
    if intent == "farewell":
        return "Goodbye! Have a great day!"
    if intent == "bot_name":
        return "I'm an AI chatbot powered by OpenAI."
    if intent == "help":
        return "Ask me anything — I use AI when things get complex!"
    return "I'm not sure I understood that."
