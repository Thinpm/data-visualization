import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from collections import Counter
import re

# Tải các tài nguyên cần thiết từ NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def get_wordnet_pos(tag):
    """Map POS tag to first character lemmatize() accepts"""
    tag_dict = {
        'J': 'a',  # Tính từ
        'N': 'n',  # Danh từ
        'V': 'v',  # Động từ
        'R': 'r'   # Trạng từ
    }
    return tag_dict.get(tag[0], 'n')  # Mặc định là danh từ

def load_text(file_path):
    """Đọc và trả về nội dung file văn bản"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def preprocess_text(text):
    """Tiền xử lý văn bản với lemmatization cải tiến"""
    # Chuyển đổi thành chữ thường
    text = text.lower()
    
    # Loại bỏ các ký tự đặc biệt và số
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Loại bỏ stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatization với pos tagging
    lemmatizer = WordNetLemmatizer()
    tagged_tokens = pos_tag(tokens)
    tokens = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) 
             for word, tag in tagged_tokens]
    
    return tokens

def combine_word_frequencies(tokens):
    """Tính tần suất của mỗi từ và kết hợp các từ trùng lặp"""
    # Sử dụng Counter để đếm tần suất
    word_freq = Counter(tokens)
    
    # Tạo text với mỗi từ chỉ xuất hiện một lần
    unique_text = ' '.join(f'{word}' for word in word_freq.keys())
    
    # Tạo từ điển tần suất cho WordCloud
    frequencies = {word: count for word, count in word_freq.items()}
    
    return unique_text, frequencies

def create_wordcloud(tokens):
    """Tạo word cloud từ các tokens với xử lý từ trùng lặp"""
    # Kết hợp tần suất từ
    unique_text, frequencies = combine_word_frequencies(tokens)
    
    # Tạo WordCloud với frequencies
    wordcloud = WordCloud(
        width=1200, 
        height=800,
        background_color='white',
        max_words=100,
        min_font_size=10,
        max_font_size=150,
        prefer_horizontal=0.7,  # Ưu tiên từ nằm ngang
        relative_scaling=0.5,   # Điều chỉnh tỷ lệ kích thước giữa các từ
        collocations=False      # Tắt collocations để tránh từ trùng lặp
    ).generate_from_frequencies(frequencies)
    
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud - Alice in Wonderland')
    plt.tight_layout(pad=0)
    plt.savefig('output/wordcloud.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_word_frequencies(tokens, top_n=20):
    """Vẽ biểu đồ tần suất từ"""
    freq_dist = nltk.FreqDist(tokens)
    top_words = freq_dist.most_common(top_n)
    
    words, frequencies = zip(*top_words)
    
    plt.figure(figsize=(12, 6))
    plt.bar(words, frequencies)
    plt.xticks(rotation=45)
    plt.title('Top {} Most Frequent Words'.format(top_n))
    plt.tight_layout()
    plt.savefig('output/word_frequencies.png')
    plt.close()

def load_glove_embeddings(file_path):
    """Tải GloVe embeddings"""
    embeddings = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            embeddings[word] = vector
    return embeddings

def plot_semantic_relationships(tokens, embeddings, top_n=20):
    """Vẽ biểu đồ quan hệ ngữ nghĩa sử dụng PCA"""
    # Lấy các từ phổ biến nhất
    freq_dist = nltk.FreqDist(tokens)
    top_words = [word for word, _ in freq_dist.most_common(top_n)]
    
    # Lấy embeddings cho các từ phổ biến
    word_vectors = []
    valid_words = []
    for word in top_words:
        if word in embeddings:
            word_vectors.append(embeddings[word])
            valid_words.append(word)
    
    if not word_vectors:
        print("Không tìm thấy embeddings cho các từ đã chọn")
        return
    
    # Giảm chiều dữ liệu xuống 2D
    pca = PCA(n_components=2)
    reduced_vectors = pca.fit_transform(word_vectors)
    
    # Vẽ biểu đồ
    plt.figure(figsize=(12, 8))
    plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1])
    
    for i, word in enumerate(valid_words):
        plt.annotate(word, (reduced_vectors[i, 0], reduced_vectors[i, 1]))
    
    plt.title('Semantic Word Relationships (PCA)')
    plt.savefig('output/semantic_relationships.png')
    plt.close()

def plot_word_similarities(tokens, embeddings, top_n=10):
    """Vẽ heatmap thể hiện độ tương đồng giữa các từ"""
    # Lấy các từ phổ biến nhất
    freq_dist = nltk.FreqDist(tokens)
    top_words = [word for word, _ in freq_dist.most_common(top_n)]
    
    # Lấy embeddings cho các từ phổ biến
    word_vectors = []
    valid_words = []
    for word in top_words:
        if word in embeddings:
            word_vectors.append(embeddings[word])
            valid_words.append(word)
    
    if not word_vectors:
        print("Không tìm thấy embeddings cho các từ đã chọn")
        return
    
    # Tính toán ma trận tương đồng cosine
    similarity_matrix = cosine_similarity(word_vectors)
    
    # Vẽ heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(similarity_matrix, 
                xticklabels=valid_words,
                yticklabels=valid_words,
                cmap='YlOrRd',
                annot=True,
                fmt='.2f')
    plt.title('Word Similarity Heatmap')
    plt.tight_layout()
    plt.savefig('output/word_similarities.png')
    plt.close()

def main():
    # Đường dẫn đến file văn bản và embeddings
    text_file = 'data/alice_in_wonderland.txt'
    glove_file = 'glove.6B.100d.txt'
    
    # Đọc và tiền xử lý văn bản
    text = load_text(text_file)
    tokens = preprocess_text(text)
    
    # Tạo các visualization
    create_wordcloud(tokens)
    plot_word_frequencies(tokens)
    
    # Tải GloVe embeddings
    embeddings = load_glove_embeddings(glove_file)
    
    # Tạo các visualization sử dụng embeddings
    plot_semantic_relationships(tokens, embeddings)
    plot_word_similarities(tokens, embeddings)

if __name__ == "__main__":
    main() 