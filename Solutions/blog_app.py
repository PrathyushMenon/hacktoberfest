import flask
from flask import request,jsonify
from werkzeug.wrappers import response
from flask_pymongo import PyMongo

app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/post_db"
mongo = PyMongo(app)

posts = [
    {
        'id':0,
        'title': 'Post !!',
        'descrption': 'Lmaoooo this the description'
    },

     {
        'id':1,
        'title': 'Post 2 !!',
        'descrption': 'Lmaoooo this the description'
    }
]

detail_post =  {
        'id':1,
        'title': 'Post 2 !!',
        'descrption': 'Lmaoooo this the descriptionasdasdkjhkajshdjkashdjkashdjkhasdkjhasjkdhjhkjhasd',
        'action':'can-read'
    }



cursor = mongo.db.posts
for document in cursor.find().add_option('post'):
    print (document)


# @app.route('/api/v1/posts', methods=['GET'])
# def api_all():
    
#     response =  jsonify(posts)
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     mongo.db.post_db.
#     return response


# @app.route('/api/v1/posts/<id>', methods=['GET'])
# def api_details():

    
#     response =  jsonify(posts)
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response


# app.run()