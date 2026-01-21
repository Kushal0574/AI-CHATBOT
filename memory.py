class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_message(self, sender: str, message: str):
        self.history.append({"role": sender, "content": message})

    def get_formatted_history(self):
        messages = [{"role": "system", "content": "You are a helpful AI chatbot."}]
        for msg in self.history:
            role = "assistant" if msg["role"] == "bot" else "user"
            messages.append({"role": role, "content": msg["content"]})
        return messages
