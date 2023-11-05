
import os
# Defining a "Extract" function that will take a pdf file as input
def Extract(pdf):
    # pip install PyPDF2
    from PyPDF2 import PdfReader


    pdfFileObj = PdfReader(pdf)

    full_text = ""
    for page in pdfFileObj.pages:
        full_text += page.extract_text()

    full_text = full_text.replace("\n", " ")
    return full_text

if __name__ == "__main__":
    filename = "ticket.pdf"
    text = Extract("ticket.pdf")
    print(text)

