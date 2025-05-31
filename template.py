#1. Importing tools we need
import os
from pathlib import Path
import logging

#2. Setting up logging 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
#[2025-05-31 18:30:00]: Creating file: README.md

#3. Naming your project
project_name = "textsummarizer"

#4. Listing the files/folders you want
list_of_files = [
    ".github/workflows/.gitkeep",
    
    # Core folders and __init__.py
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    # Config files
    "config/config.yaml",
    "params.yaml",

    # App entry points
    "app.py",
    "main.py",

    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py",
]


#5. Creating the files/folders
#Go through each file in your list (e.g., README.md, src/textsummarizer/__init__.py, etc.)
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    #If the file is in a folder, make sure the folder exists


#If the folder doesn’t exist, make it!
    if filedir != "" and not os.path.exists(filedir):
        os.makedirs(filedir)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")


#If the file doesn’t exist, create it (leave it empty for now)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
