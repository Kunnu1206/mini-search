from ranker import rank

docs = {
    1: "Python is great for search engines",
    2: "Java is great for apps",
    3: "I love Python and apps",
}

for doc_id, score in rank(docs, "python apps"):
    print(doc_id, round(score, 3), docs[doc_id])
    