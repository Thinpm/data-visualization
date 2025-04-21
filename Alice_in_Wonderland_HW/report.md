# Báo cáo Dự án: Phân tích và Trực quan hóa Văn bản Alice in Wonderland

## 1. Giới thiệu
### 1.1 Mục tiêu
- Phân tích cấu trúc và ý nghĩa của văn bản "Alice in Wonderland"
- Áp dụng các kỹ thuật xử lý ngôn ngữ tự nhiên (NLP)
- Trực quan hóa kết quả phân tích bằng các phương pháp hiện đại

### 1.2 Công nghệ sử dụng
- Python và các thư viện NLP (NLTK)
- Thư viện trực quan hóa (Matplotlib, WordCloud, Seaborn)
- GloVe embeddings cho phân tích ngữ nghĩa

## 2. Phương pháp thực hiện

### 2.1 Tiền xử lý dữ liệu
- Làm sạch văn bản: loại bỏ ký tự đặc biệt, chuyển về chữ thường
- Tokenization: tách văn bản thành các từ riêng lẻ
- Loại bỏ stopwords: loại bỏ các từ phổ biến không mang nhiều ý nghĩa
- Lemmatization: chuẩn hóa các từ về dạng gốc

### 2.2 Phân tích tần suất từ
- Đếm số lần xuất hiện của mỗi từ
- Xác định các từ xuất hiện nhiều nhất
- Trực quan hóa bằng word cloud và biểu đồ cột

### 2.3 Phân tích ngữ nghĩa
- Sử dụng GloVe embeddings để biểu diễn từ trong không gian vector
- Áp dụng PCA để giảm chiều dữ liệu
- Tính toán độ tương đồng cosine giữa các từ

## 3. Kết quả và Phân tích

### 3.1 Word Cloud
- Hiển thị trực quan tần suất từ
- Các từ quan trọng nổi bật với kích thước lớn
- Màu sắc và bố cục tối ưu cho việc quan sát

### 3.2 Biểu đồ tần suất từ
- Top 20 từ xuất hiện nhiều nhất
- So sánh tần suất giữa các từ
- Phát hiện các từ khóa chính trong văn bản

### 3.3 Biểu đồ quan hệ ngữ nghĩa
- Thể hiện mối quan hệ giữa các từ trong không gian 2D
- Các từ có nghĩa tương tự nằm gần nhau
- Phát hiện các nhóm từ có liên quan về mặt ngữ nghĩa

### 3.4 Heatmap độ tương đồng
- Ma trận tương đồng giữa các từ
- Màu sắc thể hiện mức độ tương đồng
- Xác định các cặp từ có nghĩa gần nhau

## 4. Kết luận và Đề xuất
- Dự án đã thành công trong việc phân tích và trực quan hóa văn bản
- Các visualization giúp hiểu rõ hơn về cấu trúc và nội dung của văn bản
- Có thể mở rộng dự án bằng cách:
  + Thêm các phương pháp phân tích khác
  + Tối ưu hóa các tham số trực quan hóa
  + Áp dụng cho các văn bản khác

## 5. Tài liệu tham khảo
1. NLTK Documentation: https://www.nltk.org/
2. WordCloud Documentation: https://amueller.github.io/word_cloud/
3. GloVe: Global Vectors for Word Representation: https://nlp.stanford.edu/projects/glove/ 