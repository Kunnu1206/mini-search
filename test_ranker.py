from ranker import rank

docs = {
    1: "Python is great for search engines",
    2: "Java is great for apps",
    3: "I love Python and apps",
}

def test_shorter_doc_ranks_higher():
    results = rank(docs, "python")
    assert [doc_id for doc_id, score in results] == [3, 1]

def test_doc_with_both_words_first():
    results = rank(docs, "great apps")
    assert results[0][0] == 2

def test_no_match():
    assert rank(docs, "banana") == []