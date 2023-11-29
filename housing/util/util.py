import os, sys
import yaml
from housing.exception import HousingException

def read_yml_file(file_path:str)->dict:
    """
    Reads YML file and returns the contents as a dictionary.
    file_path:str
    """
    try:
        with open(file_path, 'rb') as yml_file:
            return yaml.safe_load(yml_file)
    except Exception as e:
        raise HousingException(e, sys) from e