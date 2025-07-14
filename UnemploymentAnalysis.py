import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Loading the data
df = pd.read_csv('D:\Internship projects\Pakistan_Poverty_Dataset_2000_2023.csv')

# Step 2: Viewing basic info
print("Dataset Head:\n", df.head())
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())

# Step 3: Data Cleaning 
df.columns = [col.strip() for col in df.columns]  # removed extra spaces

# Step 4: Renaming for clarity 
if 'Year' not in df.columns:
    df.rename(columns={df.columns[0]: 'Year'}, inplace=True)
if 'Unemployment Rate' not in df.columns:
    # Trying to identify the correct column by keyword
    for col in df.columns:
        if 'unemploy' in col.lower():
            df.rename(columns={col: 'Unemployment Rate'}, inplace=True)
            break

# Step 5: Droping rows with missing values
df.dropna(subset=['Unemployment Rate'], inplace=True)

# Step 6: Converting 'Year' to integer 
df['Year'] = df['Year'].astype(int)

# Step 7: Basic Trend Analysis
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Year', y='Unemployment Rate', marker='o', color='orange')
plt.title('Unemployment Rate in Pakistan (2000–2023)', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 8: Identifying Years with Highest Unemployment
print("\nTop 5 Years with Highest Unemployment:")
print(df.sort_values(by='Unemployment Rate', ascending=False).head())

# Step 9: Correlating Check
numeric_cols = df.select_dtypes(include='number')
if len(numeric_cols.columns) > 2:
    plt.figure(figsize=(8, 5))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()
