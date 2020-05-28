from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/SignUP"
mongo = PyMongo(app)
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



if __name__ == "__main__":
    app.run(debug=True)
