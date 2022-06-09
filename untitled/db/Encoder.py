# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Encoder
   Description :
   Author :       HP
   date：          2021/3/19
-------------------------------------------------
   Change Activity:
                   2021/3/19:
-------------------------------------------------
"""
__author__ = 'HP'

import datetime
import decimal
import json


class Decimal_and_DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(o, decimal.Decimal):
            return float(o)
        else:
            return json.JSONEncoder.default(self, o)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)