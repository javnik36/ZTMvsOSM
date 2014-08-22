def server(PORT=8000):
    import http.server
    import socketserver

    
    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("Server started at port", PORT)
    httpd.serve_forever()

