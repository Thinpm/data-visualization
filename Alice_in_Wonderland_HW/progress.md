# Phân tích văn bản Alice in Wonderland sử dụng NLP và Trực quan hóa dữ liệu
Trang web: https://nlp.stanford.edu/projects/glove/

File: glove.6B.100d.txt (nằm trong file nén glove.6B.zip)

## 1. Tiền xử lý văn bản (Text Preprocessing)

### Quá trình thực hiện:
- Đọc file văn bản từ Project Gutenberg
- Chuyển đổi toàn bộ văn bản thành chữ thường
- Loại bỏ các ký tự đặc biệt và số
- Tokenize văn bản thành các từ riêng lẻ
- Loại bỏ stopwords (các từ phổ biến như "the", "a", "and",...)
- Thực hiện lemmatization (chuẩn hóa các từ về dạng gốc)

### Kết quả:
- Văn bản được làm sạch và chuẩn hóa
- Các từ được tokenize thành danh sách riêng lẻ
- Sẵn sàng cho các bước phân tích tiếp theo

## 2. Trực quan hóa tần suất từ

### 2.1 Word Cloud
- Sử dụng thư viện WordCloud
- Kích thước của mỗi từ tỷ lệ với tần suất xuất hiện
- Màu sắc ngẫu nhiên để tăng tính thẩm mỹ
- Lưu kết quả vào `output/wordcloud.png`

### 2.2 Biểu đồ cột tần suất
- Vẽ biểu đồ cột cho top 20 từ xuất hiện nhiều nhất
- Trục x: các từ
- Trục y: số lần xuất hiện
- Sử dụng matplotlib để tạo biểu đồ
- Lưu kết quả vào `output/word_frequencies.png`

### Kết quả:
- Word cloud cho cái nhìn tổng quan về tần suất từ
- Biểu đồ cột cho thấy chính xác số lần xuất hiện của mỗi từ
- Giúp xác định các từ khóa quan trọng trong văn bản

## 3. Phân tích quan hệ ngữ nghĩa sử dụng GloVe và PCA

### Quá trình thực hiện:
- Sử dụng GloVe embeddings (100 chiều)
- Chọn top 20 từ phổ biến nhất
- Giảm chiều dữ liệu xuống 2D sử dụng PCA
- Vẽ biểu đồ scatter plot với các từ được chú thích

### Kết quả:
- Biểu đồ PCA trong `output/semantic_relationships.png`
- Các từ có nghĩa tương tự sẽ nằm gần nhau trong không gian 2D
- Giúp hiểu được mối quan hệ ngữ nghĩa giữa các từ

## 4. Heatmap độ tương đồng từ

### Quá trình thực hiện:
- Chọn top 10 từ phổ biến nhất
- Tính toán ma trận tương đồng cosine giữa các từ
- Sử dụng seaborn để vẽ heatmap
- Màu sắc thể hiện mức độ tương đồng (từ 0 đến 1)

### Kết quả:
- Heatmap trong `output/word_similarities.png`
- Màu sắc càng đậm thể hiện độ tương đồng càng cao
- Giúp xác định các nhóm từ có nghĩa tương tự nhau

## Kết luận
- Dự án đã thực hiện thành công các yêu cầu về phân tích văn bản và trực quan hóa
- Các visualization giúp hiểu sâu hơn về cấu trúc và nội dung của văn bản
- Kết quả có thể được sử dụng cho các phân tích sâu hơn về ngôn ngữ và ngữ nghĩa
- Các kỹ thuật trực quan hóa được áp dụng phù hợp với mục đích phân tích dữ liệu văn bản 