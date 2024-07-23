from flask import Flask, request, jsonify

from Service import user_service
from User import User

app = Flask(__name__)

service = user_service()

@app.route('/user', methods = ['POST'])
def create_user():
    data = request.get_json()
    user = User(data['id'], data['email'], data['password'], data['role'], data['user_name'])
    service.create_user(user)
    doc_json = jsonify(user)
    print("doc json ", doc_json)
    return doc_json


@app.route('/users', methods = ['GET'])
def get_all_users():
    users_list = service.get_users()
    return users_list

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get_user(user_id)
    return user

@app.route('/')
def hello():
    return 'Your Flask Server Running'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '5001')