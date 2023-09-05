from document_header_editor import header_generator

from api import save_file

import requests
import time
import string
import random
import os
import sys
sys.path.append("..")


folder = "{}/tmp".format(os.path.dirname(__file__))

def cleanup():
    list_of_files = os.listdir("{}/out".format(folder))
    for filename in list_of_files:
        filepath = "{}/out/{}".format(folder, filename)
        modified_time=os.path.getmtime(filepath)
        if time.time()-modified_time > 600: #time in seconds
            os.remove(filepath)



def addHeader(cv):
    cleanup()

    cv_file = save_file.save_file_from_url(cv, f"{folder}/in")
    out_file = "UNABLETOGENERATE.local"

    if cv_file:
        a = header_generator.HeaderGenerator()
        a.load(f"{folder}/in/{cv_file}")
        a.set_logo_header(f"{folder}/logo.png", 1)
        out_file_name = str(''.join(random.choices(string.ascii_lowercase + string.digits, k=7))) + ".docx"
        out_file = f"{folder}/out/{out_file_name}"
        a.save(out_file)
        
    return out_file
    #return out_file_name, cv_file
    