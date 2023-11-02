from setuptools import setup

# Declaring Varibles for setup functions
PROJECT_NAME = "house-price-predictor"
VERSION="0.0.1"
AUTHOR="Vamsi Batta"
DESCRIPTION='First ML Project'


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=['housing']
)