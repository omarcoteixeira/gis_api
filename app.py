import sys
sys.settrace

import matplotlib
matplotlib.use('TkAgg')

import logging

from flask_cors import CORS
from api.document_api import document_api
from flask import (
    Flask,
)

app = Flask(__name__)
CORS(app)

app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

app.register_blueprint(document_api)


@app.route('/')
def home():
    return '', 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
