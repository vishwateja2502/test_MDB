from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Direct MongoDB Atlas URI (password is URL encoded)
mongo_uri = "mongodb+srv://vishwateja2502:vishwa%4025@cluster0.ig42emq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
db = client["loginDB"]
users_collection = db["users"]

@app.route('/')
def index():
    return render_template('login.html')  # Ensure login.html is in the templates folder

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Save login details to MongoDB
    users_collection.insert_one({'email': email, 'password': password})
    return f"Welcome {email}! Your login info was saved to MongoDB."

@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))  # Hide MongoDB _id in output
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
