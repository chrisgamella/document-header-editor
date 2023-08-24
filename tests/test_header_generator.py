import unittest
import os
import sys

sys.path.append("..")

from document_header_editor import header_generator


class TestHeaderGenerator(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources for the tests
        pass

    def tearDown(self):
        # Clean up resources after the tests
        pass

    def test_save(self):
        folder = os.path.dirname(__file__)
        a = header_generator.HeaderGenerator()
        a.load(folder + os.path.sep + "test.docx")
        a.set_logo_header(folder + os.path.sep + "logo.png", 1)
        
        out_file = folder + os.path.sep + "test_out.docx"
        if os.path.exists(out_file): os.remove(out_file)
        a.save(out_file)
        self.assertTrue(os.path.exists(out_file))


    def test_save_text_header(self):
        folder = os.path.dirname(__file__)
        a = header_generator.HeaderGenerator()
        a.load(folder + os.path.sep + "test.docx")
        
        out_file = folder + os.path.sep + "test_out.docx"
        if os.path.exists(out_file): os.remove(out_file)
        a.save(out_file)
        self.assertTrue(os.path.exists(out_file))
