#!/usr/bin/python3
"""
Starts a flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display an HTML page with list """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def tear_down_appcontext(exception):
    """ Remove the current  SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
