#!/usr/bin/env python
# -*- coding: utf-8 -*-

from session import *

content_type_html()
authenticated = is_authenticated("cookietest")

html = '<html>{0}<br /><a href="log{1}.py">{2}</a></html>'.format(
    "Bienvenido, " + get_auth_cookies("cookietest")[0] if authenticated else "",
    "out" if authenticated else "in",
    "Salir" if authenticated else "Ingresar"
)

print (html)