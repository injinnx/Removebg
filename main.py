from fastapi import FastAPI, File, UploadFile
from rembg import remove
from io import BytesIO
from fastapi.responses import StreamingResponse
import os

app = FastAPI()

@app.post("/remove-background/")
async def remove_background(file: UploadFile = File(...)):
    image = await file.read()
    output = remove(image)
    return StreamingResponse(BytesIO(output), media_type="image/png")
