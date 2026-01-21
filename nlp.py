def detect_intent(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"
    if any(word in text for word in ["bye", "goodbye"]):
        return "farewell"
    if "name" in text:
        return "bot_name"
    if "help" in text:
        return "help"

    return "unknown"
