from document_header_editor import header_generator

import os
import sys
sys.path.append("..")



def saveTmp(cv):
    cv = "test.docx"
    return cv

def test_save(cv):
    folder = "{}/tmp".format(os.path.dirname(__file__))
    a = header_generator.HeaderGenerator()
    a.load("{}/{}".format(folder, saveTmp(cv)))
    a.set_logo_header(folder + os.path.sep + "logo.png", 1)
    
    out_file = folder + os.path.sep + "test_out.docx"
    if os.path.exists(out_file): os.remove(out_file)
    a.save(out_file)
    return os.path.exists(out_file)