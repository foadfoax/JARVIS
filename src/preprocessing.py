def preprocess_text(text):
    text = text.lower()
    tokens = text.split()
    return " ".join(tokens)
