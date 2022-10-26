#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       session.py
#       
#       Copyright 2014 Recursos Python - www.recursospython.com
#       

from Cookie import SimpleCookie
from datetime import datetime, timedelta
from hashlib import md5
from os import environ


def _build_cookie(name, domain, username, password, expiration_days):
    """
    Build a SimpleCookie object and returns the HTTP
    Set-Cookie header.
    """
    cookie = SimpleCookie()
    
    # Username and Password (encrypt this one first).
    cookie[name] = username + "|" + md5(password).hexdigest()
    
    # Expiration.
    expires = datetime.now() + timedelta(days=expiration_days)
    
    # Morsel objects
    cookie[name]["domain"] = domain
    cookie[name]["path"] = "/"
    cookie[name]["expires"] = expires.strftime("%a, %d-%b-%Y "
                                               "%H:%M:%S PST")
    
    # Return HTTP header (Set-Cookie).
    return cookie


def content_type_html():
    """Prints the Content-Type header for HTML code"""
    print "Content-Type: text/html"
    print


def get_auth_cookies(name):
    """
    Return a 2-tuple (username, password) if there are
    available cookies. False otherwise.
    """
    # Check if there's any cookie available.
    if "HTTP_COOKIE" in environ:
        cookie = SimpleCookie(environ["HTTP_COOKIE"])
        # Look for our cookie
        if name in cookie:
            # Maybe it's empty
            if cookie[name].value:
                return tuple(cookie[name].value.split("|"))
    return False


def is_authenticated(name):
    """
    Return True if the HTTP cookies are set. False otherwise.
    """
    try:
        # Retrieve cookies data
        cookie_username, cookie_password = get_auth_cookies(name)
    except TypeError:
        # No cookies available
        return False
    else:
        # Security issue: should validate the cookie values.
        return True


def remove_auth_cookie(name, domain):
    """
    Remove a HTTP auth cookie.
    """
    # -1 removes the cookie
    print _build_cookie(name, domain, "", "", -1)


def set_auth_cookie(name, domain, username, password):
    """
    Set a HTTP auth cookie.
    """
    # Will expire in 7 days
    print _build_cookie(name, domain, username, password, 7)
