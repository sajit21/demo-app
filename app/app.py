# app/app.py running
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello Medium. This is sajit maharjan, a devops engineer at STARTsmall PVT. LTD!!. Just checking the workflow of argocd'
