# Cài đặt: pip install websockets nest-asyncio requests opencv-python python-dotenv
import asyncio
import websockets
import json
import requests
import cv2
import numpy as np
import nest_asyncio
import os
from dotenv import load_dotenv

load_dotenv()
nest_asyncio.apply()

FIREBASE_DB_URL = os.getenv('FIREBASE_DB_URL')

async def test_client():
    # 1. LẤY URL WEBSOCKET
    print("🔍 Đang tìm URL WebSocket từ Firebase...")
    try:
        resp = requests.get(FIREBASE_DB_URL)
        ws_url = resp.json().get("ws_url")
        if not ws_url:
            print("❌ Không tìm thấy ws_url.")
            return
        print(f"✅ Đã kết nối: {ws_url}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return

    # 2. CHUẨN BỊ ẢNH DEEPFAKE
    print("\n🖼️ Đang tải ảnh mẫu (Lena)...")
    img_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
    img_resp = requests.get(img_url)
    img_array = np.asarray(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    _, buffer = cv2.imencode('.jpg', img)
    img_bytes = buffer.tobytes()

    # 3. CHẠY TEST
    try:
        async with websockets.connect(ws_url, ping_interval=None, ping_timeout=None) as websocket:
            print("=" * 60)
            
            # --- TEST 1: CHỐNG LỪA ĐẢO VỚI NHIỀU DOMAIN ---
            test_domains = ["google.com", "http://testphp.vulnweb.com/login.php"] 
            
            for domain in test_domains:
                print(f"👉 [TEST] Đang phân tích domain: {domain}")
                await websocket.send(domain) # Gửi dạng text
                
                print("⏳ Chờ Server xử lý...")
                response_text = await websocket.recv()
                result_1 = json.loads(response_text)
                
                print(f"📩 [KẾT QUẢ - {domain}]:")
                print(json.dumps(result_1, indent=2, ensure_ascii=False))
                print("-" * 40)

            print("=" * 60)

            # --- TEST 2: DEEPFAKE ---
            print("👉 [TEST DEEPFAKE] Gửi dữ liệu ảnh (Bytes)...")
            await websocket.send(img_bytes) # Gửi dạng bytes
            
            response_bytes = await websocket.recv()
            result_2 = json.loads(response_bytes)
            print("📩 [KẾT QUẢ DEEPFAKE]:")
            print(json.dumps(result_2, indent=2, ensure_ascii=False))

            print("\n🎉 HOÀN TẤT!")

    except websockets.exceptions.ConnectionClosedError:
        print("❌ Lỗi: Server đã ngắt kết nối đột ngột.")
    except Exception as e:
        print(f"❌ Có lỗi: {e}")

asyncio.run(test_client())