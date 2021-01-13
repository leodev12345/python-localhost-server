import os
from http.server import HTTPServer, CGIHTTPRequestHandler
path=input("Enter adress of directory you want to host: ")
os.chdir(path)
port=int(input("Enter port of server: "))
server_object = HTTPServer(server_address=('', port), RequestHandlerClass=CGIHTTPRequestHandler)
print("Server started on your local network, type localhost:{your port} in your web browser")
server_object.serve_forever()
