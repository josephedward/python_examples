import os
import shutil
import json
from os import path
from flask import Flask, send_from_directory, request, jsonify
from lib.linter import linter
from lib.ot import applyOperation
app = Flask(__name__, static_url_path='', static_folder='Public')

EXTENSIONS = {
    "Java": ".java",
    "C": ".c",
    "C++": ".cpp",
    "C#": ".cs",
    "Python": ".py",
    "Ruby": ".rb",
    "Golang": ".go"
}

@app.route('/')
def public():
    return app.send_static_file('index.html')

@app.route('/api-linter/initlint', methods=['POST'])
def initlint():
    data = request.form
    tempfolder = data['folderName']
    tempfileName = tempfolder + "/Main" + EXTENSIONS[data['lang']]
    if not path.exists('temp'):
        os.mkdir('temp')
    if not path.exists(tempfolder):
        os.mkdir(tempfolder)
    result = linter(data['text'], data['lang'], tempfileName)
    if (result['status'] == 'err'):
        return jsonify(status = 'error', payload = { 'message': result['message'], 'fileName': tempfileName })
    return jsonify(status = 'ok', payload = {'fileName': tempfileName }, statusCode = 200)

@app.route('/api-linter/lint', methods=['POST'])
def lint():
    data = request.form
    tempfileName = data['fileName']
    f = open(tempfileName, 'r')
    text = f.read()
    f.close()
    text = applyOperation(text, json.loads(data['operation']))
    result = linter(text, data['lang'], tempfileName)
    if result['status'] == 'err':
        return jsonify(status = 'error', payload = { 'message': result['message'] })
    
    return jsonify(status = 'ok', statusCode = 200)

@app.route('/api-linter/removeTemp', methods=['POST'])
def removeTemp():
    folder = request.form['folderName']
    if path.exists(folder):
        shutil.rmtree(folder)
    return jsonify(status = 'ok', statusCode = 200)