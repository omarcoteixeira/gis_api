import logging
import os

from flask import Flask, make_response, jsonify, json
from services import gis as service
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

@app.route('/')
def home():
    return ''


@app.route('/document/<document_id>/default/z/x/y')
def get_map(document_id, z, x, y):
    bio = service.get_map(document_id)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=%s.png' % document_id
    return response, 200


@app.route('/document/<document_id>/ndvi/z/x/y')
def get_ndvi_map(document_id, z, x, y):
    bio = service.get_map_ndvi(document_id)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=%s.png' % document_id
    return response, 200


@app.route('/document/<document_id>/meta')
def get_metadata(document_id):
    meta = service.get_metadata(document_id)
    data = json.load(open(meta))

    return jsonify(data) if data else jsonify({}), 200


@app.route('/document/<document_id>/coordinates')
def get_coordinates(document_id):
    coordinates = service.get_coordinates(document_id)
    return jsonify(coordinates) if coordinates else jsonify({}), 200


@app.route('/document/<document_id>/histogram')
def get_histogram_map(document_id):
    bio = service.get_histogram(document_id)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=%s.png' % document_id
    return response, 200


@app.route('/document/<document_id>/layers/<layer>/z/x/y')
def get_layers_map(document_id, layer, z, x, y):
    bio = service.get_layers_map(document_id, layer)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=%s.png' % document_id
    return response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
