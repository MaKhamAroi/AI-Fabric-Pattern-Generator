from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.services import generate_image
import os

app = FastAPI(title="AI Fabric Pattern Backend")

# Serve static files (generated_images) สำหรับดาวน์โหลด
app.mount("/images", StaticFiles(directory="app/generated_images"), name="images")

# CORS สำหรับอนุญาต frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # เปลี่ยนเป็น frontend domain ใน production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
def api_generate(prompt: str = Body(..., embed=True)):
    """
    POST /generate
    Body: { "prompt": "คำอธิบายลายผ้า" }
    Returns: { "image": base64, "download_url": "/images/filename.png" }
    """
    try:
        image_base64, filename = generate_image(prompt)
        # filename เป็น path → แปลงเป็น URL สำหรับ frontend
        file_url = "/images/" + os.path.basename(filename)
        return {"image": image_base64, "download_url": file_url}
    except Exception as e:
        return {"error": str(e)}
