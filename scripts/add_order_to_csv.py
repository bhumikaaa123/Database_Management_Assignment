import csv
from datetime import datetime, timedelta
import os

# Order details
order_id = "001"
department = "Finance"
email = "finance@example.com"
file_name = "sample_order_signed.docx"
completion_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')

# CSV file path
csv_file = r'C:\Users\Bhumika\Desktop\Database_Management_Assignment\database\orders.csv'

# Check if file exists
file_exists = os.path.exists(csv_file)

# Write data
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Order ID", "Department", "Email", "File Name", "Completion Date"])
    writer.writerow([order_id, department, email, file_name, completion_date])

print("✅ Order added to CSV successfully!")
