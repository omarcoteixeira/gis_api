"""GIS module."""

import rasterio
import numpy as np
from matplotlib import pyplot as plt

from rasterio.plot import show, show_hist
from common.utils import (
    get_image_from_plot
)


TRUE_COLOR_RESOURCE_PATH = 'data/{}/true_color.tif'
BANDS_RESOURCE_PATH = 'data/{}/bands/{}.tif'
NDVI_RESOURCE_PATH = 'data/{}/ndvi.tif'


def read_document(document_id):
    path = TRUE_COLOR_RESOURCE_PATH.format(document_id)
    return rasterio.open(path)


def read_document_band(document_id, band):
    path = BANDS_RESOURCE_PATH.format(document_id, band)
    return rasterio.open(path)


def get_map(document_id):
    raster = read_document(document_id)
    plt.show = lambda: None

    show(raster.read(), title='Default')
    return get_image_from_plot()


def get_map_bands(document_id, band=None):
    raster = read_document_band(document_id, band) \
        if band else read_document(document_id)
    return raster.read()


def get_map_ndvi(document_id):
    path = _resolve_ndvi(document_id)
    raster = rasterio.open(path).read(1)
    plt.show = lambda: None

    show(raster, title='NDVI')
    return get_image_from_plot()


def get_histogram(document_id):
    raster = read_document(document_id)
    plt.show = lambda: None

    show_hist(
        raster, title='Histogram',
        histtype='stepfilled', bins=50, lw=0.0, stacked=False, alpha=0.3
    )

    return get_image_from_plot()


def get_layers_map(document_id, layer):
    raster = read_document(document_id)

    cases = {
        'reds': 1,
        'greens': 2,
        'blues': 3
    }
    case = cases[layer.lower()]
    title = layer.lower().title()

    if case:
        plt.show = lambda: None
        show(
            (raster, case),
            title=title,
            cmap=title
        )

    return get_image_from_plot()


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