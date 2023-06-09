#!/usr/bin/env python3

import sys, os
import asyncio
#, requests, json
#from dotenv import load_dotenv
from flask import *  #Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from model_constructor.models import *
from img_chk import to_chk

#load_dotenv('.env1')
#with open('.env1', 'r') as env:
#    _env = json.load(env)
#    print(_env)
#print(os.environ.get('tag1'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tskdlr.db"
#db = SQLAlchemy(app)

#class TehZadacha(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    task_id = db.Column(db.String, nullable=False)
#    descr = db.Column(db.String, nullable=False)
    #tsk_type = db.Column(db.String(10), from_choices={'FIELD': [(1, 'high'), (2, 'middle'), (3,'low')]})
#    assigned = db.Column(db.Integer)
#    datetime = db.Column(db.DateTime, default=datetime.utcnow)
#    isActive = db.Column(db.Boolean, default=True)

#    def __repe__(self):
#        return f'%s' % self.descr

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

#async def form_maket():
#    await asyncio.sleep(5)
    #app = QtWidgets.QApplication([])
    #mon = Monitor()
    #print('mon')
    #await asyncio.sleep(1)
    #return 'done'

#async def check_side():
#    print('Testirovanie')
#    await asyncio.sleep(1)
#    return 'done'

async def main():
    app.run(debug=True, port=5001)

if __name__ == '__main__':
    #print('started ...')
    asyncio.run(main())
