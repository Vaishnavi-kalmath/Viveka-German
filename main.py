from libretranslatepy import LibreTranslateAPI
from fpdf import FPDF
from PyPDF2 import PdfReader

translator = LibreTranslateAPI()

pdfFileObj = open('sample.pdf','rb')
pdfreader = PdfReader(pdfFileObj)
pdf = FPDF()
pages = len(pdfreader.pages)
for n in range(pages):
    pageObj = pdfreader.pages[n]
    extracted_text = pageObj.extract_text()
    paragraphs = extracted_text.split('\n')
    pdf.add_page()
    pdf.set_font("Arial", size= 11)
    for p in paragraphs:
        translated_text = translator.translate(p, "en", "de")
        pdf.multi_cell(0, 5, translated_text)
        pdf.ln()
pdf.output("sampleout.pdf")