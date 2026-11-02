from indexer import build_index, search

docs = {
    1: "Python is great for search engines",
    2: "Java is great for apps",
    3: "I love Python and apps",
}

def test_single_word():
    index = build_index(docs)
    assert search(index, "python") == {1, 3}

def test_two_words():
    index = build_index(docs)
    assert search(index, "python apps") == {3}

def test_missing_word():
    index = build_index(docs)
    assert search(index, "banana") == set()
    