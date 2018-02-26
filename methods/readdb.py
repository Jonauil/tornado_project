#!/usr/bin/env python
# coding=utf-8

# from db import cur
import methods.db as db

def select_read(condition,value):
    sql = "SELECT * FROM USER WHERE %s = '%s'"
    data = (condition,value)
    db.cur.execute(sql % data)
    lines = db.cur.fetchall()
    print("lines:", lines)

    num = [x[2] for x in lines]
    print("num:",num)

    return lines


def select_column(condition,table):
    sql = "SELECT %s FROM %s"
    data = (condition,table)
    db.cur.execute(sql % data)
    lines = db.cur.fetchall()
    print("select_column:",lines)
    return lines

# if __name__ == '__main__':
#     select_read(condition="username",value="huangzai")
#     select_column(condition="username",table="user")
