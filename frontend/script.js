async function generateImage() {
  const prompt = document.getElementById("prompt").value;
  const output = document.getElementById("output");
  output.innerHTML = "⏳ กำลังสร้างภาพ...";

  try {
    const response = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });

    const data = await response.json();

    if (data.image) {
      output.innerHTML = "";

      // แสดงรูป
      const img = document.createElement("img");
      img.src = "data:image/png;base64," + data.image;
      output.appendChild(img);

      // สร้างลิงก์ดาวน์โหลด
      const link = document.createElement("a");
      link.href = "http://127.0.0.1:8000" + data.download_url;
      link.innerText = "💾 ดาวน์โหลด PNG";
      link.download = "fabric.png";
      link.style.display = "block";
      link.style.marginTop = "10px";
      output.appendChild(link);

    } else {
      output.innerHTML = "❌ เกิดข้อผิดพลาด: " + (data.error || "ไม่ทราบสาเหตุ");
    }

  } catch (err) {
    output.innerHTML = "❌ เกิดข้อผิดพลาดเครือข่าย: " + err;
  }
}
