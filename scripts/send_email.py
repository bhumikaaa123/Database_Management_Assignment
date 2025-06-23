import csv
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get credentials from .env file
sender_email = os.getenv("EMAIL_USER")
app_password = os.getenv("EMAIL_PASS")

# ✅ Paths
csv_file = r'C:\Users\Bhumika\Desktop\Database_Management_Assignment\database\orders.csv'
output_folder = r'C:\Users\Bhumika\Desktop\Database_Management_Assignment\output_docs'

# ✅ Read the first order
try:
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        first_order = next(reader)
except (StopIteration, FileNotFoundError):
    print("❌ No orders found or orders.csv missing.")
    exit()

# ✅ Extract details
receiver_email = first_order['Email']
file_name = first_order['File Name']
attachment_path = os.path.join(output_folder, file_name)

# ✅ Compose the email content
subject = "Signed Order Document from Amazing Dance Academy"
body = f"""
Dear {first_order['Department']} Department,

Please find attached the digitally signed order document (Order ID: {first_order['Order ID']}).
Expected completion date: {first_order['Completion Date']}.

Regards,
Bhumika Tusamad
Amazing Dance Academy
"""

# ✅ Simulate sending the email (DO NOT actually send)
print("📤 Simulating email send...")
print("------------------------------------------------")
print(f"From: {sender_email}")
print(f"To: {receiver_email}")
print(f"Subject: {subject}")
print(f"Body:\n{body}")
print(f"Attachment: {attachment_path}")
print("✅ Email logic complete — sending skipped for security.")
