import unittest
import os
import sys

sys.path.append("..")

from pathlib import Path
import os.path

from document_header_editor import header_generator


folder = os.path.dirname(__file__)
a = header_generator.HeaderGenerator()
print(a.load(folder + os.path.sep + "test.docx"))
a.set_logo_header(folder + os.path.sep + "logo.png", 1)
print(a.save(folder + os.path.sep + "test_out.docx"))