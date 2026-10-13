import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

print("Loading combined dataset...")

df = pd.read_csv("combined_document_data.csv")
df = df.dropna(subset=["text", "label"])
df["text"] = df["text"].astype(str).str.strip()
df = df[df["text"] != ""]

print("\nRecords per category:")
print(df["label"].value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        max_features=15000,
        sublinear_tf=True
    )),
    ("classifier", MultinomialNB())
])

print("\nTraining model...")
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nAccuracy:", round(
    accuracy_score(y_test, predictions), 4
))

print("\nClassification report:")
print(classification_report(
    y_test, predictions, zero_division=0
))

with open("document_classifier.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved as document_classifier.pkl")