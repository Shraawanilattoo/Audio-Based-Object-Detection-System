import wikipedia


def search(query):
    results = wikipedia.summary(query, sentences = 3)
    print(results)
    return results