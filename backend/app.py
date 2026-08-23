from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = """
        <html>
        <head>
            <title>Freelance Project Collaboration Platform</title>
        </head>
        <body>
            <h1>Freelance Project Collaboration Platform</h1>
            <p>Backend server is running successfully.</p>
        </body>
        </html>
        """

        self.wfile.write(response.encode())


server = HTTPServer(("localhost", 8000), ServerHandler)

print("Server running at http://localhost:8000")

server.serve_forever()