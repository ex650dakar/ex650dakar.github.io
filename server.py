import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Set the current working directory to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Optional: Print the directory to verify
print("Serving from:", os.getcwd())

# Your custom handler (if you have one)
class CustomHandler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if path.lower().endswith('.stl'):
            return 'model/stl'
        return super().guess_type(path)

# Start the server
server_address = ('', 8000)
httpd = HTTPServer(server_address, CustomHandler)
print('Starting server...')
httpd.serve_forever()