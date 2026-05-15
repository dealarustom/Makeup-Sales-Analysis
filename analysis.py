import pandas as pd
df= pd.read_csv('makeup_sales_dataset_2025.csv')

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic statistics:")
print(df.describe())

# ================================
# REVENUE ANALYSIS
# ================================
print("\n--- Revenue by Brand ---")
brand_revenue = df.groupby('Brand')['Revenue_USD'].sum().sort_values(ascending=False)
print(brand_revenue)

print("\n--- Revenue by Product Type ---")
product_revenue = df.groupby('Product_Type')['Revenue_USD'].sum().sort_values(ascending=False)
print(product_revenue)

print("\n--- Revenue by Country ---")
country_revenue = df.groupby('Country')['Revenue_USD'].sum().sort_values(ascending=False)
print(country_revenue)

print("\n--- Revenue by Sales Channel ---")
channel_revenue = df.groupby('Sales_Channel')['Revenue_USD'].sum().sort_values(ascending=False)
print(channel_revenue)

import matplotlib.pyplot as plt

# ================================
# CHART 1 - Revenue by Brand
# ================================
plt.figure(figsize=(10, 6))
brand_revenue.plot(kind='bar', color='pink')
plt.title('Total Revenue by Brand')
plt.xlabel('Brand')
plt.ylabel('Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_by_brand.png')
plt.show()
print("Chart 1 saved!")

# ================================
# CHART 2 - Revenue by Country
# ================================
plt.figure(figsize=(10, 6))
country_revenue.plot(kind='bar', color='purple')
plt.title('Total Revenue by Country')
plt.xlabel('Country')
plt.ylabel('Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_by_country.png')
plt.show()
print("Chart 2 saved!")

# ================================
# CHART 3 - Revenue by Sales Channel
# ================================
plt.figure(figsize=(8, 8))
channel_revenue.plot(kind='pie', autopct='%1.1f%%')
plt.title('Revenue by Sales Channel')
plt.savefig('revenue_by_channel.png')
plt.show()
print("Chart 3 saved!")