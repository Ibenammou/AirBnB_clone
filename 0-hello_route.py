#!/usr/bin/python3
"""
Flask Web application with a route that displays "Hello HBNB"
"""

from flask import Flask

app = Flask(__name__)


# Using strict_slases=False for the route
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    class to display content
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
