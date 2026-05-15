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
# CHART - Revenue Per Capita by Country
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