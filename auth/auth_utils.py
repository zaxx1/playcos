def validate_token(token):
    return isinstance(token, str) and len(token) > 0