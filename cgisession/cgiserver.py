#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler


class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/"]


httpd = HTTPServer(("", 8000), Handler)
httpd.serve_forever()
