from pathlib import Path
import pandas as pd
import spacy
import json
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
from joblib import dump
import re
from bs4 import BeautifulSoup 

# === Step 1: Reading and parsing ===

def path_file(input_file):
    return Path(input_file).read_text(encoding='utf-8').splitlines()

def parse(line):
    parts = [p.strip() for p in line.split('|')]
    if len(parts) != 3:
        return None
    return {'data': parts[0], 'category': parts[1], 'title': parts[2]}

def convert(lines):
    news = []
    for line in lines:
        parsed = parse(line)
        if parsed:
            news.append(parsed)
    return news

def write_json(output_file, data):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# === Step 2–4: Cleaning, tokenization, counting ===

nlp = spacy.load("en_core_web_sm")

 # Якщо будуть HTML-теги

def clean_text(doc):
    """
    Cleaning up one spaCy document:
    - HTML removal
    - lemmatization
    - filtering: only words, no stop words
    """
    # 1. If you have HTML (for the future, you may not need it now)
    text = BeautifulSoup(doc.text, "html.parser").get_text()

    # 2. Reprocessing after cleaning HTML (optional)
    doc = nlp(text)

    # 3. Tokenization + filtering
    clean_tokens = [
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return clean_tokens


def tokenize_and_count(df):
    texts = df['title'].astype(str).tolist()
    all_tokens = []

    for doc in nlp.pipe(texts, disable=["parser", "ner"]):
        tokens = clean_text(doc)
        all_tokens.extend(tokens)

    word_freq = Counter(all_tokens)
    return word_freq


def plot_top_words(word_freq, top_n=20, output_img='output/top_words.png'):
    common = word_freq.most_common(top_n)
    words, freqs = zip(*common)

    plt.figure(figsize=(10, 6))
    plt.bar(words, freqs, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title(f'Top {top_n} Words')
    plt.tight_layout()
    Path(output_img).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_img)
    print(f"📈 Top words plot saved to {output_img}")
    
# === Step 5: Classification of news by category

def classify_news(df):
    # Input and output data
    X = df['title'].astype(str)
    y = df['category']

    # breakdown by train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorization
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Classifier
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    # Predict
    y_pred = model.predict(X_test_vec)

    # Metrics
    print("📊 Classification report:")
    print(classification_report(y_test, y_pred))
    
    
    dump(model, 'output/model.joblib')
    dump(vectorizer, 'output/vectorizer.joblib')
    print("💾 Model and vectorizer saved to output/")
    return model, vectorizer

# === 6
def extract_top_bigrams(news_list, top_n=20):
    """
    Extract top-N most common bigrams from news titles.
    """
    texts = [item['title'] for item in news_list]
    vectorizer = CountVectorizer(ngram_range=(2, 2), stop_words='english')
    X = vectorizer.fit_transform(texts)

    sum_words = X.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

    return words_freq[:top_n]


def plot_top_bigrams(bigram_freqs, output_img='output/top_bigrams.png'):
    """
    Plot and save top-N bigrams.
    """
    bigrams, freqs = zip(*bigram_freqs)

    plt.figure(figsize=(10, 6))
    plt.bar(bigrams, freqs, color='salmon')
    plt.xticks(rotation=45, ha='right')
    plt.title('Top 20 Bigrams')
    plt.tight_layout()
    Path(output_img).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_img)
    print(f"📈 Top bigrams plot saved to {output_img}")

# === Step 7: Main function ===

def main():
    input_path = 'data/input.txt'
    output_file = 'output/news.json'
    

    print("📥 Reading and parsing...")
    lines = path_file(input_path)
    data_news = convert(lines)
    write_json(output_file, data_news)
    print("✅ Parsing is complete. JSON saved")

    print("📊 Text processing and frequency counting...")
    df = pd.read_json(output_file)
    word_freq = tokenize_and_count(df)

    print("🔝 Top 20 words:")
    for word, freq in word_freq.most_common(20):
        print(f"{word}: {freq}")
    plot_top_words(word_freq)
    
    classify_news(df)
    
    print("🔗 Extracting and plotting top bigrams...")
    bigrams = extract_top_bigrams(data_news)
    for phrase, freq in bigrams:
        print(f"{phrase}: {freq}")
    plot_top_bigrams(bigrams)

    
    model, vectorizer = classify_news(df)

if __name__ == "__main__":
    main()
