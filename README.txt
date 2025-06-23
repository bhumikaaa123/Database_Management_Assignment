# 📚 Database Management Assignment

This project was developed by **Bhumika Tusamad** as part of the AICTE Database Management Assignment 2025.  
It automates the process of managing departmental orders using Python, including:

- PDF to Word conversion  
- Adding a digital signature  
- Department-wise data logging  
- Simulated email delivery using environment variables

---

## 📁 Project Structure

```
Database_Management_Assignment/
├── input_pdfs/              # Input order PDFs
├── output_docs/             # Output Word files (signed/unsigned)
├── database/                # Order logs (CSV)
├── scripts/                 # Python automation scripts
├── .env                     # ⚠️ Contains email credentials (DO NOT UPLOAD PUBLICLY)
├── .env.example             # Sample file for environment variables
└── README.md                # Project documentation
```

---

## 🚀 Features

| Feature                  | Description |
|--------------------------|-------------|
| 📄 PDF → Word            | Uses `pdf2docx` to convert PDFs |
| ✍️ Digital Signature     | Uses `python-docx` to add signature text |
| 📊 Order CSV Logging     | Appends structured data to `orders.csv` |
| 📧 Email (Simulated)     | Email logic implemented using `smtplib` |
| 🔐 Secure Credentials    | Email credentials stored securely via `.env` |

---

## 🛠 Libraries Required

Install these libraries before running:

```bash
pip install pdf2docx python-docx python-dotenv
```

---

## 🧪 Run Step-by-Step

1. **Create folder structure**
```bash
python scripts/create_folders.py
```

2. **Convert PDF to Word**
```bash
python scripts/convert_pdf_to_word.py
```

3. **Add digital signature to Word file**
```bash
python scripts/add_signature.py
```

4. **Store order data in database**
```bash
python scripts/add_order_to_csv.py
```

5. **Simulate sending email**
```bash
python scripts/send_email.py
```

---

## 🔐 Security Notes

- `.env` contains your **email and app password**. Never upload this file publicly.
- A `.env.example` file is provided so others can use the same structure safely:
```
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_app_password_here
```
- Email functionality is fully implemented but **not executed** during submission to protect your credentials and account security.

---

## 👩‍💻 Author

**Bhumika Tusamad**  
B.Sc. Computer Science  
AICTE Internship Assignment | 2025

---

## 📝 Disclaimer

This project is for **academic purposes only**.  
No real emails are sent — the logic is in place, but actual sending is skipped for safety.
