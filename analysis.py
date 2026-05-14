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