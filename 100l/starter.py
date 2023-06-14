#!/usr/bin/env python3

import sys, os
from flask import *
from datetime import datetime
from img_chk import to_chk

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    post = []
    SITE_TITLE = os.environ.get('site_title')
    return render_template('index.html', site_title=SITE_TITLE)

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':  
        f = request.files['file']
        f.save('img/%s' % f.filename)
        res = to_chk('img/%s' % f.filename)
        return render_template("result.html", name=f.filename, res=res)

@app.route('/file_loader', methods=['GET'])
def file_loader():
    return render_template('file_loader.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
