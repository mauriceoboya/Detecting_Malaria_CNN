from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s: %(message)s: %(levelname)s')
project_name= 'malaria_cnn'

files=[
    f".github/workflow/.gitkeep",
    f'config/config.yaml',
    f"setup.py",
    f"Research/test.ipynb",
    f"params.yaml",
    f"main.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/configuraion.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py"
]

for file in files:
    file=Path(file)
    file_dir,filename=os.path.split(file)
    
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Created directory {file_dir}")
    file_path = os.path.join(file_dir, filename)
    if not os.path.exists(file_path):
        with open(file_path ,'w') as file:
            file.write("")
            logging.info(f"Created file {filename}")