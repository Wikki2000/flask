#!/usr/bin/python3

# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a function to handle requests to that route
@app.route('/')
def hello_world():
    return 'Hello, Flask World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
