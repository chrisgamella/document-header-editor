from docx import Document
import pytesseract
from docx import Document
from PIL import Image

from document_header_editor import helper_docx


def save(src, dest, logo_path, logo_width=1, text_header='', text_font_size=13):
    doc = Document()
    img = Image.open(src)
    text = pytesseract.image_to_string(img)
    doc.add_paragraph(text)
            
    return helper_docx.save(dest, dest, logo_path, logo_width=1, text_header='', text_font_size=13)