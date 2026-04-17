def get_response(messages):
    for msg in reversed(messages):
        if msg["role"] == "user":
            return msg["content"]
    return "No user message found"