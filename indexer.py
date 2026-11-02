from tokenizer import tokenize

def build_index(documents):
    index = {}
    for doc_id, text in documents.items():
        for word in tokenize(text):
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    return index

def search(index, query):
    words = tokenize(query)
    if not words:
        return set()
    results = set(index.get(words[0], set()))
    for word in words[1:]:
        results &= index.get(word, set())
    return results
