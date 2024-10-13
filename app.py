from flask import Flask, request, jsonify, render_template
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import nltk
from nltk.corpus import stopwords

# Initialize Flask app
app = Flask(__name__)

# Download stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')

# Load 20 Newsgroups dataset
data = fetch_20newsgroups(subset='all')
documents = [doc.replace('\n', ' ') for doc in data.data]  # Clean up newlines from documents

# Preprocess documents
def preprocess_text(text):
    return ' '.join([word.lower() for word in text.split() if word.lower() not in stop_words])

documents = [preprocess_text(doc) for doc in documents]

# Create Term-Document Matrix using TF-IDF
vectorizer = TfidfVectorizer(max_df=0.05, max_features=1000, ngram_range=(1, 2))
term_doc_matrix = vectorizer.fit_transform(documents)

# Apply SVD to reduce dimensionality
svd = TruncatedSVD(n_components=10, random_state=42)
reduced_matrix = svd.fit_transform(term_doc_matrix)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get user query from request
    query = request.form['query']
    
    # Preprocess query
    processed_query = preprocess_text(query)
    
    # Transform query using the same vectorizer
    query_vector = vectorizer.transform([processed_query])
    reduced_query = svd.transform(query_vector)
    
    # Calculate cosine similarity between query and documents
    similarities = cosine_similarity(reduced_query, reduced_matrix)[0]
    top_indices = np.argsort(similarities)[-5:][::-1]
    
    # Prepare results
    results = []
    for index in top_indices:
        results.append({
            'doc_id': int(index),  # Ensure the index is a regular int type
            'content': documents[index],  # Show full content of the document
            'similarity': similarities[index]  # Ensure similarity is a regular float type
        })
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)