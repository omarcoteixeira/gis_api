
import sys
import rasterio
import numpy as np


def resolve_ndvi(document_path, ndvi_output_path):
    """
    Source: http://www.loicdutrieux.net/pyLandsat/NDVI_calc.html
    :param document_id:
    :return:
    """
    math_type = rasterio.float32

    raster_red = _read_document_band(document_path, 'B04')  # Red
    raster_nir = _read_document_band(document_path, 'B08')  # Near Infrared

    red = raster_red.read(1)
    nir = raster_nir.read(1)

    # Allow division by zero
    np.seterr(divide='ignore', invalid='ignore')
    ndvi = (nir.astype(math_type) - red.astype(math_type)) / (nir + red)

    kwargs = raster_red.meta
    kwargs.update(
        dtype=math_type,
        count=1
    )

    with rasterio.open(ndvi_output_path, 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(math_type))

    return ndvi_output_path


def _read_document_band(document_path, band):
    band_path = (document_path + '/bands/{}.tif').format(band)
    return rasterio.open(band_path)


if __name__ == "__main__":
    params = sys.argv[-2:]
    document_path, ndvi_output_path = params[0], params[1]

    ndvi_path = resolve_ndvi(document_path, ndvi_output_path)
    print('NDVI file created at: {}'.format(ndvi_path))
