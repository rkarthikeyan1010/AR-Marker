import http.server
import socketserver
import socket

def get_local_ip():
    try:
        # Get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "localhost"

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.glb': 'application/octet-stream',
    '.gltf': 'application/octet-stream',
})

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    local_ip = get_local_ip()
    print(f"\nServer is running!")
    print(f"Access the application using one of these URLs:")
    print(f"On your computer: http://localhost:{PORT}")
    print(f"On your mobile device: http://{local_ip}:{PORT}")
    print("\nMake sure your mobile device is connected to the same WiFi network as this computer.")
    httpd.serve_forever() 