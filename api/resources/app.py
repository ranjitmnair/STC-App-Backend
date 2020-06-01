import json
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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

@app.route('/signup', methods=['POST'])
def signup():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _pwd = _json['pwd']
    _regno = _json['regno']
    _year = _json['year']
    _roomno = _json['roomno']
    _domain = _json['domain']
    _number = _json['number']
    #_profile_pic = _json['profile_pic']

    
    if _name and _email and _pwd and _regno and request.method == "POST":
        hashpwd = generate_password_hash(_pwd)
        mongo.db.user.insert(
            {'name': _name, 'email': _email, 'password': hashpwd, 'regno':_regno, 'year':_year, 
            'roomno':_roomno, 'domain':_domain, 'number':_number})

        # flash(f'Account created for {user.name}!', 'success')
        return jsonify("user info added")
    return jsonify("not corekt")
    
    return 'unsucessful'

@app.route('/')
def users():
    result = mongo.db.user.find()
    return dumps(result)

@app.route('/signin/<username>/<password>',methods=['GET'])
def signin(username,password):
    dbpassword= mongo.db.user.find_one({'name':username})['password']
    result=check_password_hash(dbpassword,password)
    return str(result)

@app.route('/posts', methods=['POST'])
def posts():
    _json = request.json
    _title = _json['title']
    _domain = _json['domain']
    _category = _json['category']
    _image = _json['cover_image']
    
    if _title and request.method =='POST':
        mongo.db.user.insert(
            {
                'title':_title, 'domain':_domain, 'category':_category,
                'cover_image':_image, 
            }
        )
        return 'post added succesfully'
    return 'unsucessful'

# @app.route('/')
# def hello():
#     return jsonify("hello user")



if __name__ == "__main__":
    app.run(debug=True)
