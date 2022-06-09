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
    connection = pymysql.connect(host='122.51.127.9', user='root', passwd='xsc123456', db='monitor_sys_data', port=3306, charset='utf8')
    return connection


class Test1:
    def test_data(self,need_data):
        cur = db_connect().cursor()  # 游标(指针)cursor的方式操作数据
        sql = f"select {need_data} from monitor_data"  # sql语句
        cur.execute(sql)  # execute(query, args):执行单条sql语句
        test_data = cur.fetchall()
        cur.close()
        db_connect().close()
        return test_data


if __name__ == '__main__':
    all = Test1()
    print(all.test_data("*"))
    # content = all.test_data("*")