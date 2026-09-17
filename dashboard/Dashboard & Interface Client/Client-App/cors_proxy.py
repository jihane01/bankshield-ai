import http.server
import socketserver
import urllib.request
import ssl
import json

PORT = 8001

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Target-Url')
        self.end_headers()

    def do_POST(self):
        target_url = self.headers.get('X-Target-Url')
        
        if not target_url:
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b"Missing X-Target-Url header")
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            req = urllib.request.Request(target_url, data=post_data, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, context=ctx) as response:
                resp_data = response.read()

            self.send_response(response.status)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(resp_data)
            
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(f"Proxy error: {str(e)}".encode('utf-8'))

with socketserver.TCPServer(("", PORT), ProxyHandler) as httpd:
    print(f"CORS Proxy Server running on http://localhost:{PORT}")
    httpd.serve_forever()
