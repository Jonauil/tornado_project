#!/usr/bin/env python
#coding=utf-8

from url import url
import tornado.web
import os


settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"statics"),
    cookie_secret = "FWmzI/K8TGOiVxuq3s7O5oJE7Haf2UiQsC1rR2QKIl0=",
    xsrf_cookies = True,
    login_url = '/',
)

application = tornado.web.Application(
    handlers=url,
    **settings
)