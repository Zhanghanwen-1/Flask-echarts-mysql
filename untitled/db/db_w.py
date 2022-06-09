# -*- coding: utf-8 -*-
"""
@author: zhanghanwen
@software: PyCharm
@file: test.py
@time: 2019/10/21 18:03
"""
import pymysql
import pandas as pd


# def db_input():
#     conn = pymysql.connect(host='localhost', user='root', passwd='root', db='db_sea', port=3306, charset='utf8')
#     cur = conn.cursor()
#     file = pd.read_csv("E:\Mysearch\prac_csv/test.csv")
#     rows = file.shape[0]
#     print(rows)
#     '''
#     读取数据后得到的是索引，列名，列值，我们需要将一行一行的数据存入数据库，即需要一行一行的读值
#     因此需要遍历一行一行的数据，先看遍历数据
#     '''
#     for i in range(0, rows):
#         data = file.iloc[i]
#         print(data)
#         values = (data[0], data[1])
#         print(values)
#         sql = "insert into test(id,name) value(%s,'%s')" % values
#         print(sql)
#         cur.execute(sql)
#     conn.commit()
#     conn.close()
#
#
# if __name__ == '__main__':
#     db_input()

# 以上为测试

def db_input():
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='db_sea', port=3306, charset='utf8')
    cur = conn.cursor()
    file = pd.read_csv("E:\Mysearch\python_data/sea_data.csv")
    rows = file.shape[0]
    print(rows)
    '''
    读取数据后得到的是索引，列名，列值，我们需要将一行一行的数据存入数据库，即需要一行一行的读值
    因此需要遍历一行一行的数据，先看遍历数据
    '''
    for i in range(0, rows):
        data = file.iloc[i]
        print(data)
        values = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        print(values)
        sql = "insert into env(ad,lt,do,ph,wt,sal,chl,td) value('%s','%s',%s,%s,%s,%s,%s,%s)" % values
        print(sql)
        cur.execute(sql)
    conn.commit()
    conn.close()
    '''由csv文件导入数据库的过程中我发现在创建数据库时就必须将编码改为utf-8，不然在后期即使修改，依然会报编码的错误'''


if __name__ == '__main__':
    db_input()


