#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
# Headers
print("Content-Type: text/html")
print()
url_input = cgi.FieldStorage()
if "nombre" not in url_input:
    print("<html>¡No me has dicho tu nombre!</html>")
else:
    print("""
    <html>
    <head>
        <title>Título de la página</title>
    </head>
    <h3>Hola %s!</h3>
    </html>""" % (url_input["nombre"].value))