from flask import Flask, request, jsonify
from Service import user_service
from User import User

app = Flask(__name__)

service = user_service()

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(data['id'], data['email'], data['password'], data['role'], data['user_name'])
    service.create_user(user)
    response = jsonify(user.__dict__)
    response.status_code = 201
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/users', methods=['GET'])
def get_all_users():
    users_list = service.get_users()
    users_json = jsonify([user.__dict__ for user in users_list])
    users_json.headers['Content-Type'] = 'application/json'
    return users_json

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get_user(user_id)
    if user:
        response = jsonify(user.__dict__)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = jsonify({'message': 'User not found'})
        response.status_code = 404
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route('/')
def hello():
    return 'Your Flask Server Running'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
