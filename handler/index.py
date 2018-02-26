#!/usr/bin/env python
#coding=utf-8

from handler.base import BaseHandler
import tornado.escape
import methods.readdb as mrd

class IndexHandler(BaseHandler):
    def get(self):
        usernames = mrd.select_column(condition="username",table="user")
        one_user = usernames[0][0]
        self.render("index.html",user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        print("username:",username,"password",password)
        # user_infos = mrd.select_table(table="user",column="*",condition="username",value=username)
        user_infos = mrd.select_read(condition="username",value=username)
        print("user_infos:",user_infos)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_current_user(username)
                # self.write(username)
                self.render("user.html",users=user_infos)
                # self.render("user.html")
            else:
                self.write("-1")
        else:
            self.write("-1")
    def set_current_user(self,user):
        if user:
            self.set_secure_cookie('user',tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")
