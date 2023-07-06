import pandas as pd


# Read the JSON file
data = pd.read_json("C:/Users/rakhil/Downloads/invalid_keys_file_path(1).json", typ='series')

# Create a DataFrame from the JSON data
df = pd.DataFrame(data.items(), columns=['Key', 'Value'])

# Save the DataFrame to an Excel file
df.to_excel('C:/Users/rakhil/Downloads/output.xlsx', index=False)
