from chatbot.nlp import detect_intent
from chatbot.responses import get_fallback_response
from chatbot.memory import ConversationMemory
from chatbot.openai_client import generate_openai_response

class ChatBot:
    def __init__(self):
        self.memory = ConversationMemory()

    def get_response(self, user_input: str) -> str:
        intent = detect_intent(user_input)
        self.memory.add_message("user", user_input)

        if intent == "unknown":
            response = generate_openai_response(self.memory.get_formatted_history())
        else:
            response = get_fallback_response(intent)

        self.memory.add_message("bot", response)
        return response
