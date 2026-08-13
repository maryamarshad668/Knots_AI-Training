import re
import nltk
from nltk.corpus import movie_reviews, stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

nltk.download("movie_reviews")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)

documents = []
labels = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        text = movie_reviews.raw(fileid)
        documents.append(clean(text))
        labels.append(category)

X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=10000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

predictions = model.predict(X_test_vec)
print(classification_report(y_test, predictions))

feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

top_positive = sorted(zip(coefficients, feature_names), reverse=True)[:20]
top_negative = sorted(zip(coefficients, feature_names))[:20]

print("Top positive words:")
for coef, word in top_positive:
    print(word, coef)

print()
print("Top negative words:")
for coef, word in top_negative:
    print(word, coef)