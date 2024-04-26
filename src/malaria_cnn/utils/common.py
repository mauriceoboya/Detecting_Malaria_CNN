import os
from box.exceptions import BoxValueError
import yaml
import json
from malaria_cnn import logger
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from typing import Any
import base64
import joblib


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object
    Args:
        path_to_yaml (Path): Path to the yaml file
    Returns:
        ConfigBox: A ConfigBox object
    """
    try:
        with open(path_to_yaml,'r') as file:
            config=yaml.safe_load(file)
            logger.info(f"yaml file:{path_to_yaml} load successfully")
        return ConfigBox(config)
    except Exception as e:
        logger.error(f"yaml file:{path_to_yaml} load failed")
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created successfully")
        
@ensure_annotations
def save_json(path:Path)->ConfigBox:
    with open(path) as f:
        content=json.load(f)
    logger.info(f"json loaded successfully form:{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"data saved successfully to:{path}")

@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    logger.info(f"data loaded successfully from:{path}")
    return data

@ensure_annotations
def get_size(path:Path)->str:
    size=round(os.path.getsize(path)/1024)
    return f" ~ {size} KB"

def decodeImage(Imgstring,filename):
    imgdata = base64.b64decode(Imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(filename):
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')






