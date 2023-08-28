from pdf2docx import Converter
from document_header_editor import helper_docx


def save(src, dest, logo_path, logo_width=1, text_header='', text_font_size=13):
    cv = Converter(src)
    cv.convert(dest, start=0, end=None)
    cv.close()

    return helper_docx.save(dest, dest, logo_path, logo_width=1, text_header='', text_font_size=13)





