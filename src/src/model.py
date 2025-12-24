from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class IntentClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression(max_iter=1000)

    def train(self, texts, labels):
        vectors = self.vectorizer.fit_transform(texts)
        self.model.fit(vectors, labels)

    def predict(self, text):
        vector = self.vectorizer.transform([text])
        return self.model.predict(vector)[0]
