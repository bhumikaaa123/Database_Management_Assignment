from docx import Document
import os

# 🔁 Change this to YOUR actual absolute path
input_path = r'C:\Users\Bhumika\Desktop\Database_Management_Assignment\output_docs\sample_order.docx'
output_path = r'C:\Users\Bhumika\Desktop\Database_Management_Assignment\output_docs\sample_order_signed.docx'

# Check if file exists
if os.path.exists(input_path):
    doc = Document(input_path)

    # Add a digital signature at the end
    doc.add_paragraph("\nDigitally Signed by:\nAuthorized Signature: Bhumika Tusamad.")

    # Save the new file
    doc.save(output_path)

    print("✅ Digital signature added successfully. File saved as sample_order_signed.docx")
else:
    print("❌ Word file not found at the specified path.")
