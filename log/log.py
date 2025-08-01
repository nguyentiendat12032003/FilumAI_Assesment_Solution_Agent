import json
import os
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def save_log():
    # Load user pain point
    with open("data/input_user.json", "r", encoding="utf-8") as f:
        user_input = json.load(f)["pain_point"]

    # Load features
    with open("data/features.json", "r", encoding="utf-8") as f:
        feature_data = json.load(f)

    # Prepare corpus
    corpus = [
        f"{item['description']} {' '.join(item['keywords'])} {' '.join(item['use_cases'])} {' '.join(item['how_it_helps_examples'])}"
        for item in feature_data
    ]

    # TF-IDF similarity
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    user_vec = vectorizer.transform([user_input])
    scores = cosine_similarity(user_vec, X).flatten()

    # Tạo bản ghi log
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "pain_point": user_input,
        "matches": [
            {
                "feature_name": feature["feature_name"],
                "category": feature["category"],
                "score": round(scores[i], 4)
            }
            for i, feature in enumerate(feature_data)
        ]
    }

    # Ghi log vào file
    os.makedirs("log", exist_ok=True)
    log_file = "log/matching_log.json"

    if os.path.exists(log_file):
        with open(log_file, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=2)
    else:
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump([log_entry], f, ensure_ascii=False, indent=2)

    print("Log đã được lưu vào log/matching_log.json")

if __name__ == "__main__":
    save_log()
