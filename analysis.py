import pandas as pd
df= pd.read_csv('makeup_sales_dataset_2025.csv')
pop_df = pd.read_csv('population_data.csv')

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


country_name_mapping = {
    'USA': 'United States',
    'UK': 'United Kingdom',
    'UAE': 'United Arab Emirates',
    'Saudi Arabia': 'Saudi Arabia',
    'Germany': 'Germany',
    'France': 'France',
    'India': 'India',
    'Canada': 'Canada' }

# Apply the mapping to the sales dataset
df['Country'] = df['Country'].replace(country_name_mapping)

# Calculate total revenue by country
country_revenue = df.groupby('Country')['Revenue_USD'].sum().reset_index()

# Keep only the columns we need from population dataset
pop_df = pop_df[['Country (or dependency)', 'Population 2025']]

# Rename population country column to match
pop_df = pop_df.rename(columns={'Country (or dependency)': 'Country'})

# Merge the two datasets
merged_df = country_revenue.merge(pop_df, on='Country')

# Calculate revenue per capita
merged_df['Revenue_Per_Capita'] = merged_df['Revenue_USD'] / merged_df['Population 2025']

print(merged_df)

# ================================
# CHART 4- Revenue Per Capita by Country
# ================================
plt.figure(figsize=(10, 6))
merged_df.sort_values('Revenue_Per_Capita', ascending=False).plot(
    kind='bar',
    x='Country',
    y='Revenue_Per_Capita',
    color='mediumpurple',
    legend=False
)
plt.title('Makeup Revenue Per Capita by Country')
plt.xlabel('Country')
plt.ylabel('Revenue Per Capita (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_per_capita.png')
plt.show()
print("Per capita chart saved!")

# ================================
# CHART 5 - Revenue Trends Over Time
# ================================

# Convert Date column to datetime format so Python understands it as a date
df['Date'] = pd.to_datetime(df['Date'])

# Group by month and sum revenue
monthly_revenue = df.groupby(df['Date'].dt.to_period('M'))['Revenue_USD'].sum()

plt.figure(figsize=(12, 6))
monthly_revenue.plot(kind='line', color='hotpink', marker='o')
plt.title('Revenue Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_over_time.png')
plt.show()
print("Revenue trends chart saved!")

# ================================
# CHART 6 - Best Selling Products by Units Sold
# ================================
units_by_product = df.groupby('Product_Type')['Units_Sold'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
units_by_product.plot(kind='bar', color='mediumpurple')
plt.title('Best Selling Products by Units Sold')
plt.xlabel('Product Type')
plt.ylabel('Total Units Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('units_by_product.png')
plt.show()
print("Units by product chart saved!")

# ================================
# CHART 7 - Revenue by Payment Method
# ================================
payment_revenue = df.groupby('Payment_Method')['Revenue_USD'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
payment_revenue.plot(kind='pie', autopct='%1.1f%%', colors=['hotpink', 'mediumpurple', 'lightblue', 'lightgreen'])
plt.title('Revenue by Payment Method')
plt.ylabel('')
plt.tight_layout()
plt.savefig('revenue_by_payment.png')
plt.show()
print("Payment method chart saved!")

# ================================
# KEY METRICS / KPIs
# ================================

print("=" * 50)
print("MAKEUP SALES - KEY METRICS SUMMARY")
print("=" * 50)

# Total revenue
total_revenue = df['Revenue_USD'].sum()
print(f"\nTotal Revenue: ${total_revenue:,.2f}")

# Total units sold
total_units = df['Units_Sold'].sum()
print(f"Total Units Sold: {total_units:,}")

# Total number of transactions
total_transactions = len(df)
print(f"Total Transactions: {total_transactions:,}")

# Average revenue per transaction
avg_transaction = df['Revenue_USD'].mean()
print(f"Average Revenue Per Transaction: ${avg_transaction:,.2f}")

# Average units per transaction
avg_units = df['Units_Sold'].mean()
print(f"Average Units Per Transaction: {avg_units:,.2f}")