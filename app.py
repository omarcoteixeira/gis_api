import logging

from flask import Flask, make_response
from services import gis as service

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)


@app.route('/')
def home():
    return ''


@app.route('/document/<document_id>')
def get_map(document_id):
    bio = service.get_map(document_id)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=%s.png' % document_id
    return response


@app.route('/document/<document_id>/ndvi')
def get_ndvi_map(document_id):
    bio = service.get_map_ndvi(document_id)

    response = make_response(bio.getvalue())
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'filename=ndvi-%s.png' % document_id
    return response


@app.route('/document/<document_id>/histogram')
def get_histogram_map(document_id):
    return service.get_histogram(document_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
