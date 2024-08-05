import PyPDF2

# Open the PDF file
import pdfplumber

with pdfplumber.open('<enter pdf path>.pdf') as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

print(text)