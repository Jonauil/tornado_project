#!/usr/bin/env python
#coding=utf-8

import tornado.web
from handler.base import BaseHandler

class LogoutHandler(BaseHandler):
    def get(self):
        if self.get_argument("logout",None):
            self.clear_cookie("username")
            self.redirect("/")
