#!/usr/bin/python3
"""this is going to be my first use of flask"""
from flask import Flask
app = Flask(__name__)


# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def display_hello():
    return "Hello HBNB!"


# Route definition with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    return "HBNB"


if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
