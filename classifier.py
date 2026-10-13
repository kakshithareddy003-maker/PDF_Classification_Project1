
import pymupdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


# Training examples
texts = [
    "invoice invoice number customer payment due tax subtotal",
    "tax invoice billing details amount payable",
    "electricity bill meter reading units consumed amount due",
    "water bill monthly charges billing period",
    "receipt payment received transaction paid thank you",
    "cash receipt payment confirmation amount received"
]

labels = [
    "Invoice",
    "Invoice",
    "Bill",
    "Bill",
    "Receipt",
    "Receipt"
]


# Create and train the classification model
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(texts, labels)


# Extract text from the uploaded PDF
def extract_pdf_text(pdf_file):
    text = ""

    with pymupdf.open(
        stream=pdf_file.getvalue(),
        filetype="pdf"
    ) as document:
        for page in document:
            text += page.get_text() + "\n"

    return text


# Classify the PDF
def classify_pdf(pdf_file):
    text = extract_pdf_text(pdf_file)

    if not text.strip():
        return {
            "document_type": "No readable text found",
            "confidence": 0
        }

    probabilities = model.predict_proba([text])[0]
    best_index = probabilities.argmax()

    prediction = model.classes_[best_index]
    confidence = probabilities[best_index] * 100

    return {
        "document_type": prediction,
        "confidence": round(float(confidence), 2)
    }
