from pathlib import Path
import os.path
from document_header_editor import helper_docx


class HeaderGenerator:

    src = False
    dest = False
    file_type = False
    logo_width = False
    logo_path = False
    text = '[Set the logo or text header]'
    text_font_size = 13


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

        elif self.file_type == 'pdf':
            pass
        elif self.file_type in ['png', 'jpg']:
            pass

        return False
        
        