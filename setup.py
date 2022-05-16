from setuptools import setup
from images_utils import __version__

setup(
    name='images-utils-978',
    version=__version__,

    url='https://github.com/seppia978/images_utils',
    author='seppia978',
    author_email='samuele.poppi@uninmore.it',

    py_modules=['images_utils_978'],
    install_requires=[
        'setuptools',
        'torch',
        'torchvision',
        'Pillow'
    ],
)