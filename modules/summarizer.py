import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def summarize(sentences, clean_sentences, top_n=5):

    vectorizer = TfidfVectorizer()

    sentence_vectors = vectorizer.fit_transform(clean_sentences)

    similarity_matrix = cosine_similarity(sentence_vectors)

    graph = nx.from_numpy_array(similarity_matrix)

    scores = nx.pagerank(graph)

    ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    summary = " ".join([s for _, s in ranked[:top_n]])

    return summary