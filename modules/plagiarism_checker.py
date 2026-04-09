from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism(input_text, dataset):

    documents = dataset + [input_text]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    score = similarity.max()

    return round(score * 100, 2)