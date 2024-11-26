import os
import threading
from PIL import Image
from pystray import Icon, Menu, MenuItem
import asyncio
import websockets


# 웹소켓 서버 처리
async def websocket_handler(websocket, path):
    print("WebSocket connection established")
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            
            # 트레이 아이콘에 풍선 도움말 표시
            show_notification("시험결과가 CSI에 업로드되었습니다.", message)
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket connection closed")

async def start_websocket_server():
    print("Starting WebSocket server...")
    server = await websockets.serve(websocket_handler, "localhost", 8765)
    await server.wait_closed()


    
# 트레이 아이콘 실행
def start_tray_icon():
    global icon
    print('트레이 아이콘 실행됨')
    menu = Menu(
        MenuItem('종료', lambda: icon.stop())  # 메뉴에서 아이콘 종료
    )
    image = Image.open("z.ico")
    icon = Icon("Test Tray", image, "CTMS RPA", menu)
    icon.run()

# 트레이 아이콘 알림 표시
def show_notification(title, message):
    icon.notify(message, title)
    
# 웹소켓 서버를 백그라운드에서 실행
def start_websocket_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_websocket_server())
    
# 트레이 아이콘 종료
def stop_tray_icon():
    if icon is not None:
        icon.stop()
        print("트레이 아이콘 종료됨")

# 메인 실행
# if __name__ == "__main__":
#     # 웹소켓 서버를 별도 스레드에서 실행
#     websocket_thread = threading.Thread(target=start_websocket_thread, daemon=True)
#     websocket_thread.start()

#     # 트레이 아이콘 실행
#     start_tray_icon()
