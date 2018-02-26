#!/usr/bin/env python
#coding=utf-8

import pymysql

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='news',
    charset='utf8'
)

cur = connect.cursor()

# sql = "INSERT INTO USER  (username,password,email) VALUES ('%s','%s','%s')"
# data=('Jack','123456','jack@163.com')
# cursor.execute(sql % data)
# connect.commit()
# print("插入成功",cursor.rowcount,"条数据")