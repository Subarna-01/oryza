from fastapi import APIRouter,UploadFile
from .services import store_temp_file

disease_detection_router = APIRouter()

@disease_detection_router.post('/oryza-api/disease-detection/file-upload')
async def file_upload(file: UploadFile):
    store_temp_file(file)  
    
