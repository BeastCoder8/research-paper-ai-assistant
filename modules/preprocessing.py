import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):

    sentences = sent_tokenize(text)

    clean_sentences = []

    for sentence in sentences:

        words = sentence.lower().split()

        words = [w for w in words if w not in stop_words]

        clean_sentences.append(" ".join(words))

    return sentences, clean_sentences