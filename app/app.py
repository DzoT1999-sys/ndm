from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        xff = self.headers.get('X-Forwarded-For', 'Not-Set')
        self.wfile.write(json.dumps({"X-Forwarded-For": xff}, indent=2).encode())

    def log_message(self, format, *args):
        pass  # Отключаем шум в логах для наглядности тестов

if __name__ == '__main__':
    HTTPServer(('0.0.0.0', 80), Handler).serve_forever()
