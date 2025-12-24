import json
from preprocessing import preprocess_text
from model import IntentClassifier

with open("../data/sample_intents.json") as f:
    data = json.load(f)

texts, labels = [], []
for intent, examples in data.items():
    for ex in examples:
        texts.append(preprocess_text(ex))
        labels.append(intent)

clf = IntentClassifier()
clf.train(texts, labels)

print("Prediction:", clf.predict(preprocess_text("Hello")))
