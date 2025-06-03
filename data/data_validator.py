def validate_encoded_message(message):
    return isinstance(message, str) and len(message) > 0