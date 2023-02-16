import pandas as pd

# Read in the Excel file
df = pd.read_excel('C:\Users\rayal\Documents\Github_related\Simple-Projects\sample.xlsx')

# Remove rows with missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove unwanted columns
# df.drop(columns=['Unwanted Column 1', 'Unwanted Column 2'], inplace=True)

# Rename columns
# df.rename(columns={'Old Column Name': 'New Column Name'}, inplace=True)

# Convert data types
# df['Column Name'] = df['Column Name'].astype(str)

# Save the cleaned data to a new Excel file
df.to_excel('cleaned_sample.xlsx', index=False)
