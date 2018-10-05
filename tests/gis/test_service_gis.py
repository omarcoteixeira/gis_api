"""Module for test GIS service."""

from services import gis as service

DOCUMENT_ID = 'bd74fcb4-3f4a-4769-bc8f-a9a5c6cc8893'


def test_read_document():
    r = service.read_document(DOCUMENT_ID)
    assert r


def test_get_document_map():
    image = service.get_map(DOCUMENT_ID)
    assert image


def test_get_document_ndvi_map():
    image = service.get_map_ndvi(DOCUMENT_ID)
    assert image


# def test_get_document_band():
#     bands = service.get_map_bands(DOCUMENT_ID, band='B03')
#
#     print bands
#     assert not bands


def test_document_histogram():
    r, histogram_base64 = service.get_histogram(DOCUMENT_ID)
    assert r and histogram_base64