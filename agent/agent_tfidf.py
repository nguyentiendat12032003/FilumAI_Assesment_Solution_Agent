import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_and_suggest():
    # Load feature data
    with open("data/features.json", "r", encoding="utf-8") as f:
        feature_data = json.load(f)

    # Load user pain point
    with open("data/input_user.json", "r", encoding="utf-8") as f:
        user_input = json.load(f)["pain_point"]

    # Prepare corpus from features
    corpus = [
    f"{item['description']} {' '.join(item['keywords'])} {' '.join(item['use_cases'])} {' '.join(item['how_it_helps_examples'])}"
    for item in feature_data]


    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    user_vec = vectorizer.transform([user_input])

    # Similarity matching
    scores = cosine_similarity(user_vec, X).flatten()
    top_index = scores.argmax()
    best_match = feature_data[top_index]

    print(f"- Pain Point: \"{user_input}\"")
    print(f"  - Suggested Solution: \"{best_match['feature_name']} ({best_match['category']})\"")
    print(f"  - How it helps: {best_match['how_it_helps_examples'][0]}")

if __name__ == "__main__":
    analyze_and_suggest()