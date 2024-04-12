#!/usr/bin/python3
"""Run this script to start the Flask web application on 0.0.0.0, port 5000."""
from flask import Flask

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)