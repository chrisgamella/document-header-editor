from pathlib import Path
import os.path
from document_header_editor import helper_docx, helper_pdf, helper_scanned, helper_image




class HeaderGenerator:

    src = False
    dest = False
    file_type = False
    logo_width = False
    logo_path = False
    text = '[Set the logo or text header]'
    text_font_size = 13
    scanned_threshold = 24


    def __init__(self):
        pass

    
    def load(self, path:str):        
        if os.path.exists(path):
            file_type = Path(path).suffix
            if file_type in ['.docx', '.pdf', '.jpg', '.png']:
                self.file_type = file_type
                self.src = path

                return path

        return False
    

    def set_text_header(self, text:str):
        self.text = text


    def set_logo_header(self, path:str, width:int = 1):
        self.logo_path = path
        self.logo_width = width

        return path


    def save(self, path:str) -> bool:
        """Add header and save
        
        Args:
            path (str): Save file path.
        
        Returns:
            bool: Success or fail.
        """

        if self.file_type == '.docx':
            return helper_docx.save(self.src, path, self.logo_path, self.logo_width, self.text, self.text_font_size)

        elif self.file_type == '.pdf':
            if helper_scanned.count_characters_in_pdf(self.src) < self.scanned_threshold:
                return helper_scanned.save(self.src, path, self.logo_path, self.logo_width, self.text, self.text_font_size)
            else:
                return helper_pdf.save(self.src, path, self.logo_path, self.logo_width, self.text, self.text_font_size)
        
        elif self.file_type in ['.png', '.jpg']:

            return helper_image.save(self.src, path, self.logo_path, self.logo_width, self.text, self.text_font_size)

        return False
        
        