import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
from datetime import datetime

# Thiết lập style cho biểu đồ
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")

# Hàm định dạng số tiền
def format_currency(x, pos):
    return f'{int(x):,}'

# Đọc dữ liệu
df = pd.read_csv('data/Financials.csv')

# Làm sạch dữ liệu
# Loại bỏ dấu cách thừa trong tên cột
df.columns = df.columns.str.strip()

# Chuyển đổi các cột số tiền sang kiểu số
money_columns = ['Units Sold', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 
                'Discounts', 'Sales', 'COGS', 'Profit']

for col in money_columns:
    # Xử lý các giá trị đặc biệt như '-'
    df[col] = df[col].astype(str).str.replace('$', '').str.replace(',', '').str.replace(' ', '')
    df[col] = df[col].replace('-', '0')  # Thay thế '-' bằng '0'
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)  # Xử lý các giá trị không thể chuyển đổi

# Chuyển đổi cột ngày
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Year'] = df['Year'].astype(int)
df['Month Number'] = df['Month Number'].astype(int)

# Tạo thư mục để lưu biểu đồ
import os
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# 1. Phân tích lợi nhuận theo phân khúc thị trường
plt.figure(figsize=(12, 6))
segment_profit = df.groupby('Segment')['Profit'].sum().sort_values(ascending=False)
ax = sns.barplot(x=segment_profit.index, y=segment_profit.values)
plt.title('Tổng lợi nhuận theo phân khúc thị trường', fontsize=16)
plt.xlabel('Phân khúc', fontsize=12)
plt.ylabel('Lợi nhuận', fontsize=12)
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(FuncFormatter(format_currency))

for i, v in enumerate(segment_profit.values):
    ax.text(i, v + 0.1, f'{int(v):,}', ha='center')

plt.tight_layout()
plt.savefig('visualizations/profit_by_segment.png')
plt.close()

# 2. Phân tích lợi nhuận theo quốc gia
plt.figure(figsize=(12, 6))
country_profit = df.groupby('Country')['Profit'].sum().sort_values(ascending=False)
ax = sns.barplot(x=country_profit.index, y=country_profit.values)
plt.title('Tổng lợi nhuận theo quốc gia', fontsize=16)
plt.xlabel('Quốc gia', fontsize=12)
plt.ylabel('Lợi nhuận', fontsize=12)
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(FuncFormatter(format_currency))

for i, v in enumerate(country_profit.values):
    ax.text(i, v + 0.1, f'{int(v):,}', ha='center')

plt.tight_layout()
plt.savefig('visualizations/profit_by_country.png')
plt.close()

# 3. Phân tích lợi nhuận theo sản phẩm
plt.figure(figsize=(12, 6))
product_profit = df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
ax = sns.barplot(x=product_profit.index, y=product_profit.values)
plt.title('Tổng lợi nhuận theo sản phẩm', fontsize=16)
plt.xlabel('Sản phẩm', fontsize=12)
plt.ylabel('Lợi nhuận', fontsize=12)
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(FuncFormatter(format_currency))

for i, v in enumerate(product_profit.values):
    ax.text(i, v + 0.1, f'{int(v):,}', ha='center')

plt.tight_layout()
plt.savefig('visualizations/profit_by_product.png')
plt.close()

# 4. Phân tích lợi nhuận theo Discount Band
plt.figure(figsize=(12, 6))
discount_profit = df.groupby('Discount Band')['Profit'].sum().sort_values(ascending=False)
ax = sns.barplot(x=discount_profit.index, y=discount_profit.values)
plt.title('Tổng lợi nhuận theo mức chiết khấu', fontsize=16)
plt.xlabel('Mức chiết khấu', fontsize=12)
plt.ylabel('Lợi nhuận', fontsize=12)
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(FuncFormatter(format_currency))

for i, v in enumerate(discount_profit.values):
    ax.text(i, v + 0.1, f'{int(v):,}', ha='center')

plt.tight_layout()
plt.savefig('visualizations/profit_by_discount.png')
plt.close()

# 5. Phân tích xu hướng lợi nhuận theo thời gian
plt.figure(figsize=(14, 7))
time_profit = df.groupby(['Year', 'Month Number'])['Profit'].sum().reset_index()
time_profit['Date'] = pd.to_datetime(time_profit['Year'].astype(str) + '-' + time_profit['Month Number'].astype(str))
time_profit = time_profit.sort_values('Date')

plt.plot(time_profit['Date'], time_profit['Profit'], marker='o', linewidth=2)
plt.title('Xu hướng lợi nhuận theo thời gian', fontsize=16)
plt.xlabel('Thời gian', fontsize=12)
plt.ylabel('Lợi nhuận', fontsize=12)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_currency))
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('visualizations/profit_trend.png')
plt.close()

# 6. Phân tích tương quan giữa giá sản xuất và giá bán
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Manufacturing Price', y='Sale Price', hue='Product', size='Profit', sizes=(20, 200), alpha=0.7)
plt.title('Tương quan giữa giá sản xuất và giá bán', fontsize=16)
plt.xlabel('Giá sản xuất', fontsize=12)
plt.ylabel('Giá bán', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('visualizations/price_correlation.png')
plt.close()

# 7. Phân tích lợi nhuận theo sản phẩm và phân khúc thị trường
plt.figure(figsize=(14, 8))
segment_product_profit = df.groupby(['Segment', 'Product'])['Profit'].sum().reset_index()
pivot_table = segment_product_profit.pivot(index='Segment', columns='Product', values='Profit')
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlGnBu', linewidths=0.5)
plt.title('Lợi nhuận theo sản phẩm và phân khúc thị trường', fontsize=16)
plt.tight_layout()
plt.savefig('visualizations/segment_product_profit.png')
plt.close()

# 8. Phân tích tỷ suất lợi nhuận (Profit/Sales)
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
plt.figure(figsize=(12, 6))
margin_by_product = df.groupby('Product')['Profit_Margin'].mean().sort_values(ascending=False)
ax = sns.barplot(x=margin_by_product.index, y=margin_by_product.values)
plt.title('Tỷ suất lợi nhuận trung bình theo sản phẩm', fontsize=16)
plt.xlabel('Sản phẩm', fontsize=12)
plt.ylabel('Tỷ suất lợi nhuận (%)', fontsize=12)
plt.xticks(rotation=45)

for i, v in enumerate(margin_by_product.values):
    ax.text(i, v + 0.5, f'{v:.2f}%', ha='center')

plt.tight_layout()
plt.savefig('visualizations/profit_margin_by_product.png')
plt.close()

# 9. Phân tích doanh số theo quốc gia và sản phẩm
plt.figure(figsize=(14, 8))
country_product_sales = df.groupby(['Country', 'Product'])['Sales'].sum().reset_index()
pivot_table = country_product_sales.pivot(index='Country', columns='Product', values='Sales')
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlOrRd', linewidths=0.5)
plt.title('Doanh số theo quốc gia và sản phẩm', fontsize=16)
plt.tight_layout()
plt.savefig('visualizations/country_product_sales.png')
plt.close()

# 10. Phân tích số lượng bán theo mức chiết khấu
plt.figure(figsize=(12, 6))
units_by_discount = df.groupby('Discount Band')['Units Sold'].sum().sort_values(ascending=False)
ax = sns.barplot(x=units_by_discount.index, y=units_by_discount.values)
plt.title('Số lượng bán theo mức chiết khấu', fontsize=16)
plt.xlabel('Mức chiết khấu', fontsize=12)
plt.ylabel('Số lượng bán', fontsize=12)
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(FuncFormatter(format_currency))

for i, v in enumerate(units_by_discount.values):
    ax.text(i, v + 0.1, f'{int(v):,}', ha='center')

plt.tight_layout()
plt.savefig('visualizations/units_by_discount.png')
plt.close()

# 11. Biểu đồ tròn phân bố doanh số theo phân khúc thị trường
plt.figure(figsize=(10, 8))
segment_sales = df.groupby('Segment')['Sales'].sum()
plt.pie(segment_sales, labels=segment_sales.index, autopct='%1.1f%%', startangle=90, shadow=True, explode=[0.05]*len(segment_sales))
plt.title('Phân bố doanh số theo phân khúc thị trường', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.savefig('visualizations/sales_distribution_by_segment.png')
plt.close()

# 12. Phân tích chi phí sản xuất (COGS) theo sản phẩm và quốc gia
plt.figure(figsize=(14, 8))
cogs_by_product_country = df.groupby(['Product', 'Country'])['COGS'].sum().reset_index()
pivot_table = cogs_by_product_country.pivot(index='Product', columns='Country', values='COGS')
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='Blues', linewidths=0.5)
plt.title('Chi phí sản xuất theo sản phẩm và quốc gia', fontsize=16)
plt.tight_layout()
plt.savefig('visualizations/cogs_by_product_country.png')
plt.close()

# 13. Phân tích lợi nhuận theo tháng và năm - PHIÊN BẢN TIẾNG VIỆT
plt.figure(figsize=(16, 9))

# Tạo biểu đồ đường cho từng năm
years = sorted(df['Year'].unique())

# Tên tháng tiếng Việt
month_names_vn = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 
                  'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']

# Màu sắc và marker khác nhau cho mỗi năm
colors = ['#2E8B57', '#FF6347']  # Xanh lá, Đỏ cà chua
markers = ['o', 's']  # Tròn, Vuông

for i, year in enumerate(years):
    year_data = df[df['Year'] == year]
    # Group by Month Number và tính tổng profit
    monthly_profit = year_data.groupby('Month Number')['Profit'].sum()
    
    if len(monthly_profit) > 0:
        plt.plot(monthly_profit.index, monthly_profit.values, 
                marker=markers[i], linewidth=4, label=f'Năm {year}', 
                markersize=10, color=colors[i], markerfacecolor=colors[i],
                markeredgecolor='white', markeredgewidth=2)

plt.title('Lợi nhuận theo tháng và năm', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Tháng', fontsize=16, fontweight='bold')
plt.ylabel('Lợi nhuận (VND)', fontsize=16, fontweight='bold')

# Set x-axis với tên tháng tiếng Việt
plt.xticks(range(1, 13), month_names_vn, rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_currency))

# Cải thiện lưới và legend
plt.grid(True, linestyle='--', alpha=0.7, linewidth=1)
plt.legend(fontsize=14, loc='upper left', frameon=True, fancybox=True, shadow=True)

# Thêm ghi chú giải thích
plt.figtext(0.5, 0.02, 'Ghi chú: Năm 2013 chỉ có dữ liệu từ tháng 9 (quý 4)', 
           ha='center', fontsize=12, style='italic', color='gray')

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.savefig('visualizations/profit_by_month_year.png', dpi=300, bbox_inches='tight', 
           facecolor='white', edgecolor='none')
plt.close()

# 14. Phân tích mối quan hệ giữa số lượng bán và lợi nhuận
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Units Sold', y='Profit', hue='Product', size='Sale Price', sizes=(20, 200), alpha=0.7)
plt.title('Mối quan hệ giữa số lượng bán và lợi nhuận', fontsize=16)
plt.xlabel('Số lượng bán', fontsize=12)
plt.ylabel('Lợi nhuận', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('visualizations/units_profit_relationship.png')
plt.close()

# 15. So sánh doanh số và lợi nhuận theo phân khúc thị trường
plt.figure(figsize=(14, 6))
segment_comparison = df.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
segment_comparison = segment_comparison.sort_values('Sales', ascending=False)

x = np.arange(len(segment_comparison))
width = 0.35

fig, ax = plt.subplots(figsize=(14, 6))
rects1 = ax.bar(x - width/2, segment_comparison['Sales'], width, label='Doanh số')
rects2 = ax.bar(x + width/2, segment_comparison['Profit'], width, label='Lợi nhuận')

ax.set_title('So sánh doanh số và lợi nhuận theo phân khúc thị trường', fontsize=16)
ax.set_xlabel('Phân khúc thị trường', fontsize=12)
ax.set_ylabel('Giá trị', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(segment_comparison['Segment'])
ax.legend()
ax.yaxis.set_major_formatter(FuncFormatter(format_currency))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{int(height):,}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90)

autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('visualizations/sales_profit_comparison.png')
plt.close()

print("Đã tạo xong các biểu đồ trực quan hóa!")
print("✅ Đã sửa biểu đồ profit_by_month_year.png!") 