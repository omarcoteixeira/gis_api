
from flask import (
    Blueprint,
    make_response,
    jsonify,
    json,
    send_file
)
from services import gis as service

document_api = Blueprint('document_api', __name__)


@document_api.route("/document")
def root():
    return '', 200


@document_api.route('/document/<document_id>/tms/<z>/<x>/<y>')
def get_map(document_id, z, x, y):
    bio = service.get_tile_path(document_id, z, x, y)

    return send_file(
        bio,
        mimetype='image/png'
    ) if bio else jsonify({}), 200


@document_api.route('/document/<document_id>/ndvi/<z>/<x>/<y>')
def get_ndvi_map(document_id, z, x, y):
    bio = service.get_tile_path(document_id, z, x, y, ndvi=True)

    return send_file(
        bio,
        mimetype='image/png'
    ) if bio else jsonify({}), 200


@document_api.route('/document/<document_id>/meta')
def get_metadata(document_id):
    meta = service.get_metadata(document_id)
    data = json.load(open(meta))

    return jsonify(data) if data else jsonify({}), 200


@document_api.route('/document/<document_id>/coordinates')
def get_coordinates(document_id):
    coordinates = service.get_coordinates(document_id)
    return jsonify(coordinates) if coordinates else jsonify({}), 200


@document_api.route('/document/<document_id>/histogram')
def get_histogram_map(document_id):
    bio = service.get_histogram(document_id)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=%s.png' % document_id
    return response, 200


@document_api.route('/document/<document_id>/layers/<layer>/z/x/y')
def get_layers_map(document_id, layer, z, x, y):
    bio = service.get_layers_map(document_id, layer)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=%s.png' % document_id
    return response, 200
