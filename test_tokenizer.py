from tokenizer import tokenize

def test_removes_punctuation():
    assert tokenize("Hello, World!") == ["hello", "world"]

def test_removes_stop_words():
    assert tokenize("The cat is in the house") == ["cat", "house"]

def test_empty_text():
    assert tokenize("") == []