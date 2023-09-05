from flask import Flask, request, jsonify, send_file
from api import main


import os
import sys
sys.path.append("..")



def reply(message='', data=[], success=True, statusCode=200):
    return jsonify(
        success = success,
        message = message,
        data = data,
        statusCode = statusCode
    ), statusCode



app = Flask(__name__)



@app.route('/addheader/<path:url>', methods=['GET'])
def addheader(url):
    #outf, inf =  main.addHeader(url)
    #return reply('ok', (outf, inf))
    
    #download
    return send_file(main.addHeader(url), as_attachment=True)
    


@app.route('/fetchurl/<path:url>', methods=['GET'])
def fetchurl(url):
    return reply(url)



#http://localhost:5000/addheader/http%3A%2F%2Fjobsglobal.com%2Fapp02%2Ffs1%2Fe%2Fact%2Fget%2Fname%2F1591733_CV_1591733.docx
#http://localhost:5000/addheader/https://jobsglobal.com/tree/bd3/c53cb946a6be64f6fc310835d.pdf
