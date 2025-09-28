import requests
import base64
import os

# URL ของ Stable Diffusion WebUI API
SD_API_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# โฟลเดอร์เก็บไฟล์ output
OUTPUT_DIR = "app/generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_image(prompt: str, steps: int = 20, width: int = 512, height: int = 512):
    """
    ส่ง prompt ไปยัง SD API → รับภาพ base64 → save เป็นไฟล์ PNG
    """
    payload = {
        "prompt": prompt,
        "steps": steps,
        "width": width,
        "height": height
    }

    response = requests.post(SD_API_URL, json=payload)
    response.raise_for_status()
    result = response.json()
    image_base64 = result["images"][0]

    # Save เป็นไฟล์ PNG
    safe_name = "".join([c if c.isalnum() else "_" for c in prompt[:20]])
    filename = os.path.join(OUTPUT_DIR, f"{safe_name}.png")
    image_bytes = base64.b64decode(image_base64)
    with open(filename, "wb") as f:
        f.write(image_bytes)

    return image_base64, filename
