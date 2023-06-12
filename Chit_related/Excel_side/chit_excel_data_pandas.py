import pandas as pd

# Set the range of cells to read
start_row = 3  # Change this to the row number of the first cell in the column
end_row = 32  # Change this to the row number of the last cell in the column
columns = 'B'  # Change this to the letter of the column you want to read
num_rows = end_row - start_row + 1
# Read the Excel file
df = pd.read_excel('chit_data.xlsx', sheet_name='Sheet2', usecols=columns, skiprows=list(range(1, start_row)), nrows=num_rows)

# Loop through the data and print each cell's value
for value in df[columns]:
    print(value)
