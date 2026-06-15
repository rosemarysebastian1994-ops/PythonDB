import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display data
print(df)

# Basic operations
print(df.head())        # First rows
print(df['Age'].mean()) # Average age