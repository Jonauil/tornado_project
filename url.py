#!/usr/bin/env python
#coding=utf8

import importlib,sys
importlib.reload(sys)

from handler.index import IndexHandler
from handler.user import UserHandler
from handler.logout import LogoutHandler
url = [
    (r"/",IndexHandler),
    (r"/user",UserHandler),
    (r"logout",LogoutHandler)
]