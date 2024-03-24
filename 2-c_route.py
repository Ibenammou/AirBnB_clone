#!/usr/bin/python3
"""
Script to handle dynamic routes
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns - Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return 'HBNB'


@app.route('/custom404', strict_slashes=False)
def custom404():
    """ Route to trigger a 404 error """
    return render_template('404.html'), 404


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Replace underscores with spaces"""
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
