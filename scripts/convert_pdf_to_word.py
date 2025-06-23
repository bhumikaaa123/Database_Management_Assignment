from pdf2docx import Converter
import os

# Input and Output paths
input_path = 'input_pdfs/sample_order.pdf'
output_path = 'output_docs/sample_order.docx'


# Convert PDF to Word
if os.path.exists(input_path):
    cv = Converter(input_path)
    cv.convert(output_path)
    cv.close()
    print("✅ Conversion complete. Word file saved in output_docs/")
else:
    print("❌ PDF file not found at", input_path)
