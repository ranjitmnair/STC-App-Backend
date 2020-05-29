import json
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)


app.config['MONGO_URI'] = "mongodb://localhost:27017/SignUP"

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
        now=datetime.now()
        today=now.strftime("%d/%m/%Y %H:%M:%S")
        mongo.db.resources.insert({'domain':domain,'title':title,'datetime': today,'link1':link1,'link2':link2,'link3':link3})
        return jsonify(domain+" resource added")    
    return jsonify("error") 
@app.route('/resources/<domain>')
def display(domain):
    result=mongo.db.resources.find({'domain':domain})    
    response=dumps(result)
    return response       

#notifs route
@app.route('/notifications',methods=['GET','POST'])
def create():
    _json=request.json
    title=_json['title']
    _id=_json['id'] # id such as events meetings etc.
    body=_json['body'] # content of the notif.

    if title and id and body and request.method=="POST":
        now=datetime.now()
        today=now.strftime("%d/%m/%Y %H:%M:%S")
        mongo.db.notifications.insert({'date':today,'title':title,'id':_id,'body':body})
        result=mongo.db.notifications.find({'date':today})
        response=dumps(result)
        return response
       # return "notif added"
    return jsonify("err")

# @app.route('/')
# def hello():
#     return jsonify("hello user")



if __name__ == "__main__":
    app.run(debug=True)
