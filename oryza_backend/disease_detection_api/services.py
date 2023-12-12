import shutil
import os
from fastapi import UploadFile


def store_temp_file(file: UploadFile):
    
    recieved_filename = str(file.filename)  
    temp_filepath = f'{os.path.join(os.getcwd(),"disease_detection_api","temp_img_dump")}/{recieved_filename}'
    
    with open(temp_filepath,'wb') as f:
        shutil.copyfileobj(file.file,f)


def destroy_temp_file(filepath: str):
    os.remove(filepath)