"""GIS module."""
import matplotlib
matplotlib.use('TkAgg')

import rasterio
import numpy as np
import matplotlib as plt

from rasterio.plot import show, show_hist, get_plt
from common.utils import (
    make_image_from_arrays,
    get_image_from_plot
)


TRUE_COLOR_RESOURCE_PATH = 'data/{}/true_color.tif'
BANDS_RESOURCE_PATH = 'data/{}/bands/{}.tif'
NDVI_RESOURCE_PATH = 'data/{}/ndvi.tif'

# TRUE_COLOR_RESOURCE_PATH = '../data/{}/true_color.tif'
# BANDS_RESOURCE_PATH = '../data/{}/bands/{}.tif'
# NDVI_RESOURCE_PATH = '../data/{}/ndvi.tif'


def read_document(document_id):
    path = TRUE_COLOR_RESOURCE_PATH.format(document_id)
    return rasterio.open(path)


def read_document_band(document_id, band):
    path = BANDS_RESOURCE_PATH.format(document_id, band)
    return rasterio.open(path)


def get_map(document_id):
    raster = read_document(document_id)
    return make_image_from_arrays(raster.read())


def get_map_bands(document_id, band=None):
    raster = read_document_band(document_id, band) \
        if band else read_document(document_id)
    return raster.read()


def get_map_ndvi(document_id):
    path = _resolve_ndvi(document_id)
    raster = rasterio.open(path)

    return make_image_from_arrays(raster.read())


def get_histogram(document_id):
    raster = read_document(document_id)
    figure = get_plt().gca()

    show_hist(
        raster, title='Histogram',
        histtype='stepfilled', bins=50, lw=0.0, stacked=False, alpha=0.3,
        ax=figure
    )

    return raster, get_image_from_plot()


def show_layers(document_id):
    raster = read_document(document_id)

    return raster


def _resolve_ndvi(document_id):
    """
    Source: http://www.loicdutrieux.net/pyLandsat/NDVI_calc.html
    :param document_id:
    :return:
    """
    math_type = rasterio.float32

    raster_red = read_document_band(document_id, 'B04')  # Red
    raster_nir = read_document_band(document_id, 'B08')  # Near Infrared

    red = raster_red.read(1)
    nir = raster_nir.read(1)

    # Allow division by zero
    np.seterr(divide='ignore', invalid='ignore')
    ndvi = (nir.astype(math_type) - red.astype(math_type)) / (nir + red)

    output = NDVI_RESOURCE_PATH.format(document_id)

    kwargs = raster_red.meta
    kwargs.update(
        dtype=math_type,
        count=1
    )

    with rasterio.open(output, 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(math_type))

    return output