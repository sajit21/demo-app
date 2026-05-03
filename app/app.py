# app/app.py running here
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello Medium!!'
