from setuptools import setup
from typing import List



# Declaring Varibles for setup functions
PROJECT_NAME = "house-price-predictor"
VERSION="0.0.1"
AUTHOR="Vamsi Batta"
DESCRIPTION='First ML Project'
REQUIREMENTS_FILE  = "requirements.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE) as requirements_file:
        requirements_file.readlines() 



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=['housing'],
    install_requires=get_requirements_list()
)
