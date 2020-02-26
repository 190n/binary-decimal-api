#!/usr/bin/env python3

from http.server import HTTPServer, CGIHTTPRequestHandler

DEFAULT_PORT = 8000


def run_server(port):
    CGIHTTPRequestHandler.cgi_directories = ['/scripts']
    server = HTTPServer(('', port), CGIHTTPRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutting down server')


run_server(DEFAULT_PORT)
