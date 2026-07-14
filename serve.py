#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///
"""
DOOM - Web Edition 로친 서버

사용법:
    uv run serve.py          # 기본 포트 8080
    uv run serve.py 3000     # 포트 지정
"""

import http.server
import os
import sys
import threading
import webbrowser

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        if "--verbose" in sys.argv:
            super().log_message(format, *args)


def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")


print(f"💀 DOOM Web Edition")
print(f"   서버 주소: http://localhost:{PORT}")
print(f"   종료: Ctrl+C")
print()

threading.Timer(0.5, open_browser).start()

try:
    with http.server.HTTPServer(("", PORT), QuietHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n서버를 종료합니다.")
