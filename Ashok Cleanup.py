import pandas as pd

# Load your data from the CSV file
df = pd.read_csv('Ashok.csv')

# Step 1: Remove the specified phrases from the scheme column
df['scheme'] = df['scheme'].str.replace(r'\s*\(\s*Non\s*-\s*Demat\s*', '', regex=True)
df['scheme'] = df['scheme'].str.replace(r'\s*\(Transferor scheme\)', '', regex=True)
df['scheme'] = df['scheme'].str.replace(r'\(Non-Demat', '', regex=True)  # Remove " (Non-Demat"
df['scheme'] = df['scheme'].str.replace(r'  \(Non-Demat', '', regex=True)  # Remove "  (Non-Demat"
df['scheme'] = df['scheme'].str.replace(r'\(erstwhile HDFC Index Fund - Sensex Plus Plan merged\)', '', regex=True)
df['scheme'] = df['scheme'].str.replace(r'\(erstwhile.*?\)', '', regex=True)  # Remove any brackets with the word 'erstwhile'

# Step 2: Trim white spaces from all string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Step 3: Standardize scheme names based on the reference file (if needed)
# Example: scheme_mapping = {'Aditya Birla Sun Life NASDAQ 100 FOF Direct Growth': 'Aditya Birla Sun Life NASDAQ 100 FOF Direct Growth'}
# df['scheme'] = df['scheme'].replace(scheme_mapping)

# Step 4: Clean up scheme column if needed
df['scheme'] = df['scheme'].str.replace(r'\[\*\*\*\]', '', regex=True).str.strip()

# Step 5: Filter out rows that are not required (like STT_TAX)
df = df[~df['type'].str.contains('STT_TAX', na=False)]

# Convert the 'Date' column to datetime format, inferring the format for each element
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)

# Format the date to 'dd-Mmm-yyyy'
df['date'] = df['date'].dt.strftime('%d-%b-%Y')

# Rename columns to match the desired output
df = df.rename(columns={
    'amc': 'AMC Name', 
    'scheme': 'Scheme Name', 
    'folio': 'Folio Number', 
    'date': 'Date', 
    'description': 'Transaction', 
    'amount': 'Amount', 
    'units': 'Units hold', 
    'nav': 'Price', 
    'type': 'Unit Balance',
    'isin': 'ISIN'
})

# Reorder the columns to the desired output format
df = df[['AMC Name', 'Scheme Name', 'Folio Number', 'Date', 'Transaction', 'Amount', 'Units hold', 'Price', 'Unit Balance', 'ISIN']]

# Step 7: Save the cleaned data back to CSV
df.to_csv('Ashok_Cleaned.csv', index=False)

# Print the cleaned DataFrame for verification
#print(df)
