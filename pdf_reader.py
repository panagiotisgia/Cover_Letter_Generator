import fitz # PyMuPDF

def extract_text_from_pdf(pdf_path:str):
    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        text = ""
        # Iterate over each page in the PDF
        for page in pdf:
            # Extract text from the page
            text += page.get_text()
        return text