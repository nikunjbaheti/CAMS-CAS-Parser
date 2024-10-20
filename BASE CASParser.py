import casparser
import csv
from datetime import datetime

# Read CAS PDF file
data = casparser.read_cas_pdf("Ashok.pdf", "ashok123")

# Get transactions data in CSV string format
csv_str = casparser.read_cas_pdf("Ashok.pdf", "ashok123", output="csv")

# Convert the CSV string to a list of dictionaries
csv_reader = csv.DictReader(csv_str.splitlines())

# List of columns to exclude
exclude_columns = ['pan', 'advisor', 'isin', 'amfi', 'dividend', 'balance']

# Filter the rows and exclude unwanted columns
filtered_data = []
for row in csv_reader:
    if row['type'] != 'STAMP_DUTY_TAX':
        filtered_row = {key: value for key, value in row.items() if key not in exclude_columns}
        filtered_data.append(filtered_row)

# Generate a filename with current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"transaction_data_{current_datetime}.csv"

# Get the headers from the first row of the filtered data
headers = filtered_data[0].keys() if filtered_data else []

# Save the filtered CSV data to a file
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(filtered_data)

print(f"CSV data saved to {filename}")