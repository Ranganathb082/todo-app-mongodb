from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from methods.validate  import *

app = Flask(__name__)

# Connect to your MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    hashed_password = generate_password_hash(password, method='sha256')

    user = {
        'username': username,
        'password': hashed_password
    }

    if (
        not validate_username(username) or
        not validate_password(password) or
        len(set(username.lower())) < 5
    ):
        return jsonify(message='Invalid username or password'), 400

    if db.users.find_one({'username': username}):
        return jsonify(message='Username already exists'), 400
    
    
    flag = db.users.insert_one(user)


    if flag:
        return jsonify(message='User registered successfully')
    else:
         return jsonify(message='Failed User Registration'), 401


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = db.users.find_one({'username': username})

    if user and check_password_hash(user['password'], password):
        return jsonify(message='Login successful')
    else:
        return jsonify(message='Invalid credentials'), 401


@app.route('/dbs', methods=['GET'])
def list_dbs():
    # Get a list of collections in the database
    databases = client.list_database_names()
    # collections = db.list_collection_names()

    return jsonify(databases=databases)
    

@app.route('/collections', methods=['GET'])
def list_collections():
    # Get a list of collections in the database
    collections = db.list_collection_names()

    return jsonify(collections=collections)


@app.route('/insert/<collection_name>', methods=['POST'])
def insert_data(collection_name): 
    data = request.get_json()  # Assuming the data is sent as JSON in the request body

    # Insert the data into the specified collection
    result = db[collection_name].insert_one(data)

    return jsonify(inserted_id=str(result.inserted_id))


@app.route('/update/<collection_name>/<document_id>', methods=['PUT'])
def update_document(collection_name, document_id):
    data = request.get_json()

    # Update the document in the specified collection
    result = db[collection_name].update_one({'_id': document_id}, {'$set': data})

    if result.matched_count == 1:
        return jsonify(message='Document updated successfully')
    else:
        return jsonify(message='Document not found or update failed'), 404


if __name__ == '__main__':
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    app.run(debug=True)
