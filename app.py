import http.server
import socketserver
import socket
import webbrowser
import threading
import os


PUBLIC_DIR = os.path.join(os.path.dirname(__file__), "public")


def get_lan_ip() -> str:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "127.0.0.1"


def open_browser(url: str) -> None:
    timer = threading.Timer(0.8, lambda: webbrowser.open(url))
    timer.daemon = True
    timer.start()


def run_server(port: int = 0) -> None:
    os.chdir(PUBLIC_DIR)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
        bound_port = httpd.server_address[1]
        lan_ip = get_lan_ip()
        url = f"http://127.0.0.1:{bound_port}/"
        print("\n粉色旋转玫瑰已启动：")
        print(f"  本机: {url}")
        print(f"  手机同局域网访问: http://{lan_ip}:{bound_port}/\n")
        open_browser(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n已关闭服务器，再见~")


if __name__ == "__main__":
    run_server()


