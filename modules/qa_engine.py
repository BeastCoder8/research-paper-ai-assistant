from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def answer_question(question, document):

    sentences = document.split(".")

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(sentences + [question])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    index = similarity.argmax()

    return sentences[index]