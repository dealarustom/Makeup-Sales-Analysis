import pandas as pd
df= pd.read_csv('makeup_sales_dataset_2025.csv')

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())