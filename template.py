## this is the file to create a template of the project autometically not manulally
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componenets/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    'app.py',
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath) # create a path as per the os (as all os have different paths)
    filedir,filename = os.path.split(filepath) # seperates directory and filename

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): ## create file if file is not or it is empty
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file {filepath}")
    else:
        logging.info(f"{filename} already exist")
