# คู่มือรันโปรเจกต์ AI Fabric Generator (Local)
## "AI-Fabric-Pattern-Generator"  
version: 1  
สำหรับใช้งานแบบ local โดยใช้ stable diffusion API 

## เตรียมเครื่อง
- OS: Windows   
- Python: 3.10+    
- Stable Diffusion WebUI: รันพร้อม API (txt2img) อยู่บนเครื่อง  
- VS Code: สำหรับแก้ไขไฟล์  

## เริ่มใช้งาน  
เปิด terminal → เข้าโฟลเดอร์ backend → เปิดใช้งาน environment   
- venv\Scripts\activate  

## รัน backend  
- uvicorn app.main:app --reload --host 0.0.0.0 --port 8000  

## ปิดโปรเจกต์  
- ปิด backend: CTRL+C  
- ปิด virtual environment: deactivate  
