import json
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)


app.config['MONGO_URI'] = "mongodb+srv://stcapp:stcappbackend@cluster0-zjxyv.mongodb.net/master?retryWrites=true&w=majority"

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
    return jsonify(response)       





@app.route('/posts/upload', methods=['POST'])
def posts():
    _json = request.json
    photos = request.files['photos']
    
    if request.method =="POST":
        mongo.save_file(photos.filename, photos)
        now=datetime.now()
        today=now.strftime("%d/%m/%Y %H:%M:%S")
        mongo.db.posts.insert(
            {
                'date':today,'filename': photos.filename    
            }
        )
        return jsonify('post added succesfully')
    return jsonify('unsucessful')

@app.route('/posts/<filename>')
def getposts(filename):
    return mongo.send_file(filename)


if __name__ == "__main__":
    app.run(debug=True)
