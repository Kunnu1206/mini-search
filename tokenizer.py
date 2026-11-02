import re

STOP_WORDS = {"the", "is", "a", "an", "and", "of", "to", "in", "it"}

def tokenize(text):
    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)
    return [w for w in words if w not in STOP_WORDS]