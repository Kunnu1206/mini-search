import math
from collections import Counter
from tokenizer import tokenize

def build_tf(documents):
    return {doc_id: Counter(tokenize(text)) for doc_id, text in documents.items()}

def rank(documents, query):
    tf = build_tf(documents)
    total_docs = len(documents)
    scores = {}

    for word in tokenize(query):
        docs_with_word = [d for d in tf if word in tf[d]]
        if not docs_with_word:
            continue
        idf = math.log(total_docs / len(docs_with_word)) + 1
        for d in docs_with_word:
            doc_length = sum(tf[d].values())
            score = (tf[d][word] / doc_length) * idf
            scores[d] = scores.get(d, 0) + score

    return sorted(scores.items(), key=lambda item: item[1], reverse=True)