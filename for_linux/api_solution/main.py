from fastapi import FastAPI
from fastapi.responses import StreamingResponse

import cv2 
from PIL import Image
from typing import Generator
import io

cap = cv2.VideoCapture(0)

app = FastAPI()

async def get_image_from_camera():
    #tr, frame = cap.read()
    for _ in range(10):
        return b'fake bytes'

@app.get('/img/')
async def test():
    return StreamingResponse(get_image_from_camera())

@app.get('/')
def test():
    return {"ok":"ok"}

@app.get('/kill')
def test():
    cap.release()
    return {"ok":"unalived"}

@app.get('/restart')
def test():
    cap = cv2.VideoCapture()
    return {"ok":"alived"}


