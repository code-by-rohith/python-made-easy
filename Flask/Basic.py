from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Define the Marshmallow schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # Optional: Load instances of the User class instead of dictionaries

# Initialize the schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Endpoint to create a new user
@app.route('/user', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']

    new_user = User(name, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

if __name__ == "__main__":
    # Create the database within the application context
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)
