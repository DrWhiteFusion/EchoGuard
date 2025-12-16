import PyPDF2

pdf_path = r"c:\Users\Sai_Sudarshan_S\OneDrive\Documents\GitHub\EchoGuard\Echo Guard.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    print(text)