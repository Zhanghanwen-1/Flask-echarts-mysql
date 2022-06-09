# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     db_connect
   Description :
   Author :       HP
   date：          2021/3/19
-------------------------------------------------
   Change Activity:
                   2021/3/19:
-------------------------------------------------
"""
__author__ = 'HP'

import pymysql


def db_connect():
    connection = pymysql.connect(host='localhost', user='root', passwd='root', db='db_sea', port=3306, charset='utf8')
    return connection


class Comp_data:
    def comp_data(self,need_data):
        cur = db_connect().cursor()  # 游标(指针)cursor的方式操作数据
        sql = f"select {need_data} from env"  # sql语句
        cur.execute(sql)  # execute(query, args):执行单条sql语句
        comp_data = cur.fetchall()
        cur.close()
        db_connect().close()
        return comp_data


class Tao:
    def tao_data(self, need_data):
        cur = db_connect().cursor()  # 游标(指针)cursor的方式操作数据
        sql = f"select {need_data} from env where ad='桃花'"  # sql语句
        cur.execute(sql)  # execute(query, args):执行单条sql语句
        tao_data = cur.fetchall()
        cur.close()
        db_connect().close()
        return tao_data


class Dong:
    def dong_data(self, need_data):
        cur = db_connect().cursor()  # 游标(指针)cursor的方式操作数据
        sql = f"select {need_data} from env where ad='东极'"  # sql语句
        cur.execute(sql)  # execute(query, args):执行单条sql语句
        dong_data = cur.fetchall()
        cur.close()
        db_connect().close()
        return dong_data


class Sheng:
    def sheng_data(self, need_data):
        cur = db_connect().cursor()  # 游标(指针)cursor的方式操作数据
        sql = f"select {need_data} from env where ad='嵊泗'"  # sql语句
        cur.execute(sql)  # execute(query, args):执行单条sql语句
        sheng_data = cur.fetchall()
        cur.close()
        db_connect().close()
        return sheng_data


if __name__ == '__main__':
    all = Comp_data()
    print(all.comp_data("*"))
    # content = all.comp_data("*")