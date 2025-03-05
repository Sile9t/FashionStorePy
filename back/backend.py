import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Файл для хранения данных
db_file = "data.json"

# Загружаем данные из файла
try:
    with open(db_file, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"products": [], "cart": [], "favourites": []}

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
    def do_GET(self):
        if self.path == "/products":
            self._set_headers()
            self.wfile.write(json.dumps(data["products"]).encode("utf-8"))
        elif self.path == "/cart":
            self._set_headers()
            self.wfile.write(json.dumps(data["cart"]).encode("utf-8"))
        elif self.path == "/favourites":
            self._set_headers()
            self.wfile.write(json.dumps(data["favourites"]).encode("utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = json.loads(self.rfile.read(content_length))
        
        if self.path == "/cart":
            data["cart"].append(post_data)
            self._save_data()
            self._set_headers(201)
            self.wfile.write(json.dumps({"message": "Added to cart"}).encode("utf-8"))
        elif self.path == "/favourites":
            data["favourites"].append(post_data)
            self._save_data()
            self._set_headers(201)
            self.wfile.write(json.dumps({"message": "Added to favourites"}).encode("utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode("utf-8"))
    
    def _save_data(self):
        with open(db_file, "w") as f:
            json.dump(data, f, indent=4)

# Запуск сервера
server_address = ('', 8080)
httpd = HTTPServer(server_address, RequestHandler)
print("Server running on port 8080...")
httpd.serve_forever()
