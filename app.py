import os
from flask import Flask, render_template, url_for, request
from flask import jsonify
from profanity_check import predict
from abuse_checker import *

    
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])

def index():
    if request.method == 'POST':
        text = str(request.form['text'])
        if check_abuse(text) == "Okay":
            report = "This text doesn't contain any abuse"
        else:
            report = "This text contains an abuse"
        return render_template('index.html', report=report)
    return render_template('index.html', report = "")

@app.route('/text',methods=['POST'])
def text():
    text = str(request.form['text'])
    if check_abuse(text) == "Okay":
        report = "This text doesn't contain any abuse"
    else:
        report = "This text contains an abuse"
    return jsonify(Text=report)
if __name__ == "__main__":
    app.run(debug=True)
