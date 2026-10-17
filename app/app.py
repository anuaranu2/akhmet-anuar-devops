from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        student = os.getenv("STUDENT_NAME", "Anuar Akhmet")
        message = f"Hello from Docker!\nStudent: {student}\nDevOps Laboratory\n"

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8080), MyHandler)

print("Server running on port 8080", flush=True)
server.serve_forever()
