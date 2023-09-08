from document_header_editor import header_generator

from api import save_file, config


import requests
import time
import string
import random
import os
import sys
sys.path.append("..")


folder = os.path.join(os.path.dirname(__file__), 'tmp')
#folder = config.tmp_folder


def cleanup():
    list_of_files = os.listdir(os.path.join(folder, 'out'))
    for filename in list_of_files:
        filepath = os.path.join(folder, 'out', filename)
        modified_time=os.path.getmtime(filepath)
        if time.time()-modified_time > 600: #time in seconds
            os.remove(filepath)



def addHeader(cv):
    cleanup()

    cv_file = save_file.save_file_from_url(cv, os.path.join(folder, 'in'))
    out_file = os.path.join(folder, 'UNABLETOGENERATE.local')

    if cv_file:
        a = header_generator.HeaderGenerator()
        a.load(os.path.join(folder, 'in', cv_file))
        a.set_logo_header(os.path.join(folder, 'logo.png'), 1)
        out_file_name = str(''.join(random.choices(string.ascii_lowercase + string.digits, k=7))) + ".docx"
        out_file = os.path.join(folder, 'out', out_file_name)
        a.save(out_file)

    return out_file
    #return out_file_name, cv_file
    