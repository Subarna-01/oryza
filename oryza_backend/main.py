from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from disease_detection_api.routes import disease_detection_router

app = FastAPI()
app.include_router(disease_detection_router)

origins = [ '*' ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)