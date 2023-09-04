from flask import Flask, request, jsonify
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



@app.route('/addheader/<cv>')
def addheader(cv):
    return reply(cv, main.test_save(cv))