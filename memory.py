import json
import os
import logging

# Setup logging (writes to file, not console)
logging.basicConfig(
    filename="memory.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def sanitize_messages(messages):
    """Ensure messages follow correct structure"""
    cleaned = []

    if not isinstance(messages, list):
        return []

    for msg in messages:
        if not isinstance(msg, dict):
            continue

        role = msg.get("role", "")
        content = msg.get("content", "")

        # Fix types
        role = str(role)
        content = str(content)

        if role and content:
            cleaned.append({
                "role": role,
                "content": content
            })

    return cleaned


def load_memory():
    if not os.path.exists("memory.json"):
        return []

    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # Sanitize loaded data
        return sanitize_messages(data)

    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        return []

    except Exception as e:
        logging.error(f"Unexpected load error: {e}")
        return []


def save_memory(messages):
    try:
        # Clean before saving
        messages = sanitize_messages(messages)

        # Optional: limit size
        messages = messages[-20:]

        # Safe write (prevents corruption)
        temp_file = "memory_temp.json"

        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2)

        os.replace(temp_file, "memory.json")

    except Exception as e:
        logging.error(f"Save error: {e}")