import json
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import date

app = Flask(__name__)


app.config['MONGO_URI'] = "mongodb://localhost:27017/Resources"

mongo = PyMongo(app)
#domains= webdev,appdev,ml,design
@app.route('/resources/<domain>/upload',methods=['POST'])
def upload(domain):
    _json=request.json
    title=_json['title']
    link1=_json['link1']
    link2=_json['link2']
    link3=_json['link3']

    if title and (link1 or link2 or link3) and request.method=="POST":
        today=date.today()
        if domain=="appdev":
            mongo.db.appdev.insert({'title':title,'date':today, 'link1':link1,'link2':link2,'link3':link3})
        elif domain=="webdev":
            mongo.db.webdev.insert({'title':title,'date':today,'link1':link1,'link2':link2,'link3':link3})
        elif domain=="ml":
            mongo.db.ml.insert({'title':title,'date':today,'link1':link1,'link2':link2,'link3':link3})
        elif domain=="design":
            mongo.db.design.insert({'title':title,'date':today,'link1':link1,'link2':link2,'link3':link3})
        else:
            mongo.db.misc.insert({'title':title,'date':today,'link1':link1,'link2':link2,'link3':link3})#misc resources
        return jsonify(domain+" resource added")
    else:
        return jsonify("error") 
@app.route('/resources/<domain>')
def display(domain):
    if domain=="appdev":
        result=mongo.db.appdev.find()
    elif domain=="webdev":
        result=mongo.db.webdev.find()
    elif domain=="ml":
        result=mongo.db.ml.find()
    elif domain=="design":
        result=mongo.db.design.find()
    else:
        result=mongo.db.misc.find()#misc resources
    
    response=dumps(result)
    return response       

if __name__ == "__main__":
    app.run(debug=True)