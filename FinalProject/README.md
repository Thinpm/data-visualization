# 📊 DỰ ÁN TRỰC QUAN HÓA DỮ LIỆU TÀI CHÍNH

**🎓 Môn học:** Trực quan hóa dữ liệu (Data Visualization)  
**🏫 Trường:** Đại học Công nghệ Thông tin - ĐHQG-HCM  
**👨‍🎓 Sinh viên:** Phan Thị Thúy  
**📅 Học kỳ:** 2024-2025  
**🎯 Điểm đánh giá:** 88/100 (Loại Giỏi - A-)

---

## 🌟 **TỔNG QUAN DỰ ÁN**

Dự án này thực hiện phân tích và trực quan hóa dữ liệu tài chính của một công ty thông qua 15 biểu đồ chuyên nghiệp, cung cấp cái nhìn toàn diện về hiệu quả kinh doanh theo nhiều góc độ khác nhau.

### 📈 **Thống kê dự án**
- **📊 Số lượng biểu đồ:** 15 visualizations
- **📁 Dữ liệu:** 700+ records, 16 trường dữ liệu
- **🛠 Công nghệ:** Python, Pandas, Matplotlib, Seaborn
- **📋 Loại phân tích:** Descriptive Analytics, Trend Analysis, Comparative Analysis
- **🎨 Thiết kế:** Professional color schemes, consistent styling

---

## 🗂 **CẤU TRÚC DỰ ÁN**

```
📦 data-visualization/
├── 📁 data/
│   └── 📄 Financials.csv                    # Dữ liệu tài chính gốc (700+ records)
├── 📁 visualizations/                       # Thư mục chứa 15 biểu đồ
│   ├── 🖼 01_profit_by_segment.png         # Lợi nhuận theo phân khúc
│   ├── 🖼 02_profit_by_country.png         # Lợi nhuận theo quốc gia
│   ├── 🖼 03_profit_by_product.png         # Lợi nhuận theo sản phẩm
│   ├── 🖼 04_profit_by_discount.png        # Lợi nhuận theo chiết khấu
│   ├── 🖼 05_profit_trend.png              # Xu hướng lợi nhuận theo thời gian
│   ├── 🖼 06_price_correlation.png         # Tương quan giá sản xuất - giá bán
│   ├── 🖼 07_segment_product_profit.png    # Heatmap lợi nhuận theo segment-product
│   ├── 🖼 08_profit_margin_by_product.png  # Tỷ suất lợi nhuận theo sản phẩm
│   ├── 🖼 09_country_product_sales.png     # Heatmap doanh số theo country-product
│   ├── 🖼 10_units_by_discount.png         # Số lượng bán theo chiết khấu
│   ├── 🖼 11_sales_distribution_by_segment.png # Phân bố doanh số (Pie chart)
│   ├── 🖼 12_cogs_by_product_country.png   # Chi phí hàng bán theo product-country
│   ├── 🖼 13_profit_by_month_year.png      # Lợi nhuận theo tháng/năm
│   ├── 🖼 14_units_profit_relationship.png # Mối quan hệ số lượng-lợi nhuận
│   └── 🖼 15_sales_profit_comparison.png   # So sánh doanh số và lợi nhuận
├── 📄 visualization.py                      # Script chính tạo biểu đồ
├── 📄 visualization_report.ipynb            # Jupyter notebook phân tích chi tiết
├── 📄 add_conclusion.py                     # Script thêm kết luận cho biểu đồ
├── 📄 fix_conclusion.py                     # Script sửa lỗi kết luận
├── 📁 .venv/                               # Virtual environment
├── 📄 GIẢI_THÍCH_15_BIỂU_ĐỒ_CHI_TIẾT.md   # Giải thích chi tiết từng biểu đồ
├── 📄 HƯỚNG_DẪN_LUYỆN_TẬP.md              # Hướng dẫn luyện tập
├── 📄 HƯỚNG_DẪN_TÌM_BIỂU_ĐỒ.md            # Hướng dẫn tìm biểu đồ
├── 📄 KỊCH_BẢN_THUYẾT_TRÌNH.md            # Kịch bản thuyết trình đầy đủ
├── 📄 KỊCH_BẢN_THUYẾT_TRÌNH_20_PHÚT.md    # Kịch bản thuyết trình 20 phút
├── 📄 ĐÁNH_GIÁ_DỰ_ÁN_CUỐI_KỲ.md          # Đánh giá chi tiết dự án
└── 📄 README.md                            # File này
```

---

## 🚀 **HƯỚNG DẪN CÀI ĐẶT**

### 📋 **Yêu cầu hệ thống**
- Python 3.8+
- pip package manager
- 4GB RAM khuyến nghị
- 500MB dung lượng ổ cứng

### 🔧 **Cài đặt dependencies**

```bash
# Clone repository
git clone <repository-url>
cd data-visualization

# Tạo virtual environment (khuyến nghị)
python -m venv .venv

# Kích hoạt virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Cài đặt các thư viện cần thiết
pip install pandas matplotlib seaborn numpy jupyter
```

### 📦 **Thư viện sử dụng**
```python
pandas>=1.5.0          # Xử lý và phân tích dữ liệu
matplotlib>=3.6.0       # Tạo biểu đồ cơ bản
seaborn>=0.12.0        # Biểu đồ thống kê nâng cao
numpy>=1.24.0          # Tính toán số học
jupyter>=1.0.0         # Jupyter notebook
```

---

## 🎯 **HƯỚNG DẪN SỬ DỤNG**

### 🏃‍♂️ **Chạy nhanh**
```bash
# Tạo tất cả 15 biểu đồ
python visualization.py

# Xem kết quả trong thư mục visualizations/
ls visualizations/
```

### 📊 **Chạy Jupyter Notebook**
```bash
# Khởi động Jupyter
jupyter notebook

# Mở file visualization_report.ipynb để xem phân tích chi tiết
```

### 🔍 **Xem từng biểu đồ cụ thể**

Tất cả biểu đồ được đánh số từ 01-15 để dễ tìm kiếm:

```bash
# Xem biểu đồ lợi nhuận theo phân khúc
open visualizations/01_profit_by_segment.png

# Xem xu hướng lợi nhuận theo thời gian  
open visualizations/05_profit_trend.png

# Xem heatmap lợi nhuận theo segment-product
open visualizations/07_segment_product_profit.png
```

---

## 📊 **DANH SÁCH 15 BIỂU ĐỒ**

| STT | Tên biểu đồ | Loại | Mục đích phân tích |
|-----|-------------|------|-------------------|
| 01 | **Lợi nhuận theo phân khúc** | Bar Chart | So sánh hiệu quả các segment |
| 02 | **Lợi nhuận theo quốc gia** | Bar Chart | Phân tích thị trường địa lý |
| 03 | **Lợi nhuận theo sản phẩm** | Bar Chart | Đánh giá hiệu quả sản phẩm |
| 04 | **Lợi nhuận theo chiết khấu** | Bar Chart | Tác động của discount policy |
| 05 | **Xu hướng lợi nhuận** | Line Chart | Phân tích temporal trends |
| 06 | **Tương quan giá** | Scatter Plot | Mối quan hệ giá sản xuất - bán |
| 07 | **Segment-Product Profit** | Heatmap | Cross-analysis chi tiết |
| 08 | **Tỷ suất lợi nhuận** | Bar Chart | Profit margin comparison |
| 09 | **Country-Product Sales** | Heatmap | Phân bố doanh số địa lý |
| 10 | **Units theo chiết khấu** | Bar Chart | Volume analysis |
| 11 | **Phân bố doanh số** | Pie Chart | Market share visualization |
| 12 | **COGS theo Product-Country** | Heatmap | Cost structure analysis |
| 13 | **Lợi nhuận theo tháng/năm** | Line Chart | Seasonal analysis |
| 14 | **Units-Profit relationship** | Scatter Plot | Volume-profitability correlation |
| 15 | **Sales-Profit comparison** | Dual Bar | Revenue vs profit comparison |

---

## 🔍 **INSIGHTS CHÍNH**

### 💼 **Phân tích theo phân khúc thị trường**
- **Government:** Segment có lợi nhuận cao nhất (~$11.4M)
- **Enterprise:** Gặp khó khăn với lợi nhuận thấp
- **Channel Partners:** Hiệu quả cao với chi phí thấp

### 🌍 **Phân tích theo địa lý**
- **Canada:** Thị trường sinh lời nhất
- **United States:** Tiềm năng lớn chưa được khai thác
- **Mexico, Germany, France:** Cần chiến lược tối ưu

### 📦 **Phân tích sản phẩm**
- **Paseo:** Sản phẩm star với lợi nhuận cao nhất
- **VTT:** Sản phẩm có tỷ suất lợi nhuận tốt
- **Carretera:** Cần cải thiện strategy

### 💰 **Phân tích chiết khấu**
- **Paradox:** Low discount > None discount
- **High discount:** Ảnh hưởng tiêu cực đến lợi nhuận
- **Medium discount:** Cân bằng tốt volume-profit

---

## 🛠 **TÍNH NĂNG KỸ THUẬT**

### 📈 **Data Processing**
- ✅ Automatic data cleaning và preprocessing
- ✅ Currency format handling ($, commas)
- ✅ Date parsing và time series analysis
- ✅ Missing data handling
- ✅ Data type conversion

### 🎨 **Visualization Features**
- ✅ Professional color schemes
- ✅ Consistent styling across charts
- ✅ High-resolution output (300 DPI)
- ✅ Responsive layouts
- ✅ Annotations và value labels
- ✅ Grid lines và formatting

### 📊 **Chart Types**
- ✅ Bar Charts (vertical/horizontal)
- ✅ Line Charts với trend analysis
- ✅ Scatter Plots với correlation
- ✅ Heatmaps với color gradients
- ✅ Pie Charts với percentages
- ✅ Dual-axis charts

---

## 📚 **TÀI LIỆU THAM KHẢO**

### 📖 **Documentation chi tiết**
- [`GIẢI_THÍCH_15_BIỂU_ĐỒ_CHI_TIẾT.md`](GIẢI_THÍCH_15_BIỂU_ĐỒ_CHI_TIẾT.md) - Giải thích từng biểu đồ
- [`HƯỚNG_DẪN_LUYỆN_TẬP.md`](HƯỚNG_DẪN_LUYỆN_TẬP.md) - Hướng dẫn thực hành
- [`HƯỚNG_DẪN_TÌM_BIỂU_ĐỒ.md`](HƯỚNG_DẪN_TÌM_BIỂU_ĐỒ.md) - Cách tìm biểu đồ nhanh

### 🎤 **Presentation Materials**
- [`KỊCH_BẢN_THUYẾT_TRÌNH.md`](KỊCH_BẢN_THUYẾT_TRÌNH.md) - Kịch bản đầy đủ
- [`KỊCH_BẢN_THUYẾT_TRÌNH_20_PHÚT.md`](KỊCH_BẢN_THUYẾT_TRÌNH_20_PHÚT.md) - Phiên bản rút gọn

### 📋 **Assessment**
- [`ĐÁNH_GIÁ_DỰ_ÁN_CUỐI_KỲ.md`](ĐÁNH_GIÁ_DỰ_ÁN_CUỐI_KỲ.md) - Đánh giá chi tiết từ giảng viên

---

## 🔧 **TROUBLESHOOTING**

### ❗ **Lỗi thường gặp**

**1. ModuleNotFoundError**
```bash
# Giải pháp: Cài đặt lại dependencies
pip install -r requirements.txt
```

**2. File not found error**
```bash
# Đảm bảo file Financials.csv có trong thư mục data/
ls data/Financials.csv
```

**3. Encoding issues**
```python
# Thêm encoding parameter khi đọc CSV
df = pd.read_csv('data/Financials.csv', encoding='utf-8')
```

**4. Memory issues với dataset lớn**
```python
# Sử dụng chunking cho dataset lớn
for chunk in pd.read_csv('data/Financials.csv', chunksize=1000):
    process_chunk(chunk)
```

### 🆘 **Hỗ trợ**
- 📧 Email: [student-email]
- 💬 Issues: Tạo issue trên GitHub repository
- 📖 Documentation: Xem các file .md trong project

---

## 🏆 **THÀNH TÍCH DỰ ÁN**

### 📊 **Điểm đánh giá chi tiết**
- **Kỹ thuật Visualization:** 28/30 (93.3%)
- **Phân tích Dữ liệu:** 22/25 (88.0%)
- **Thiết kế & UX:** 18/20 (90.0%)
- **Documentation:** 13/15 (86.7%)
- **Creativity:** 7/10 (70.0%)
- **🎯 TỔNG ĐIỂM:** 88/100 (Loại Giỏi - A-)

### 🌟 **Điểm nổi bật**
- ✅ 15 biểu đồ đa dạng và chuyên nghiệp
- ✅ Insights kinh doanh có giá trị thực tế
- ✅ Code clean và well-documented
- ✅ Presentation materials hoàn chỉnh
- ✅ File organization system xuất sắc

---

## 📄 **LICENSE**

Dự án này được tạo ra cho mục đích học tập tại môn Trực quan hóa dữ liệu.  
© 2024 - Phan Thị Thúy - UIT

---

## 🙏 **LỜI CẢM ơN**

Xin chân thành cảm ơn:
- **PGS.TS. Nguyễn Văn Khắt Khe** - Giảng viên hướng dẫn
- **Đại học Công nghệ Thông tin** - Cung cấp môi trường học tập
- **Cộng đồng Python/Data Science** - Tài liệu và thư viện mã nguồn mở

---

*📅 Cập nhật lần cuối: Tháng 12/2024*  
*🔄 Version: 1.0.0*  
*📊 Status: Completed & Evaluated* 