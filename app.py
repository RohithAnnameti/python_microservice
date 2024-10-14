# microservice.py
from flask import Flask, jsonify, request
app = Flask(__name__)
# Route for the home endpoint
@app.route('/')
def home():
   return "Welcome to the Python Microservice!"
# Route for greeting a user by name
@app.route('/greet', methods=['GET'])
def greet_user():
   # Get the user's name from the query parameters
   name = request.args.get('name', 'World')
   return jsonify(message=f"Hello, {name}!")
# Route for handling a post request
@app.route('/data', methods=['POST'])
def post_data():
   # Receive JSON data from the request body
   data = request.json
   return jsonify(received=data)
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
