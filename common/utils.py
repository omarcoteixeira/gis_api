"""Utils module."""
import base64
import numpy as np

from PIL import Image
from io import BytesIO
from rasterio.plot import get_plt


def get_image_from_plot(file_format='tiff'):
    ib = BytesIO()
    plt = get_plt()

    plt.savefig(ib, format=file_format)
    plt.close()
    ib.seek(0)

    return ib


def get_base64_from_plot(file_format='png'):
    return base64.b64encode(get_image_from_plot(file_format).getvalue())


def make_image_from_path(path):
    image = Image.open(path)

    bio = BytesIO()
    image.save(bio, 'JPEG')

    return bio


def make_image_from_arrays(bands, mode='RGB'):
    images = [_make_image(arr) for arr in bands]
    image = Image.merge(mode, images) if len(images) > 1 else images[0]

    bio = BytesIO()
    image.save(bio, 'PNG')

    return bio


def _make_image(arr):
    return Image.fromarray(arr.astype(np.float32)).convert('L')
