# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     util.py
   Description :
   Author :       HP
   date：          2021/3/20
-------------------------------------------------
   Change Activity:
                   2021/3/20:
-------------------------------------------------
"""
__author__ = 'HP'

#  合并两个字典
import json

from db.Encoder import Decimal_and_DateEncoder
from db.to_dict import tao_one_dict, dong_one_dict, sheng_one_dict, comp_one_dict


def merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def merge_inv(dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8,):
    dict_inv = {}
    dict_inv.update(dict1)
    dict_inv.update(dict2)
    dict_inv.update(dict3)
    dict_inv.update(dict4)
    dict_inv.update(dict5)
    dict_inv.update(dict6)
    dict_inv.update(dict7)
    dict_inv.update(dict8)
    return dict_inv


def dict_to_json(dict_data):
    axis_value = json.dumps(dict_data, cls=Decimal_and_DateEncoder)
    return axis_value


def taohua():
    ad = tao_one_dict("ad")
    xlt = tao_one_dict("lt")
    ydo = tao_one_dict("do")
    yph = tao_one_dict("ph")
    ywt = tao_one_dict("wt")
    ysal = tao_one_dict("sal")
    ychl = tao_one_dict("chl")
    ytd = tao_one_dict("td")
    taohua_data = merge_inv(ad, xlt, ytd, ydo, yph, ychl, ysal, ywt)

    return taohua_data



def dongji():
    ad = dong_one_dict("ad")
    xlt = dong_one_dict("lt")
    ydo = dong_one_dict("do")
    yph = dong_one_dict("ph")
    ywt = dong_one_dict("wt")
    ysal = dong_one_dict("sal")
    ychl = dong_one_dict("chl")
    ytd = dong_one_dict("td")
    dongji_data = merge_inv(ad, xlt, ytd, ydo, yph, ychl,  ysal, ywt)
    return dongji_data


def shengsi():
    ad = sheng_one_dict("ad")
    xlt = sheng_one_dict("lt")
    ydo = sheng_one_dict("do")
    yph = sheng_one_dict("ph")
    ywt = sheng_one_dict("wt")
    ysal = sheng_one_dict("sal")
    ychl = sheng_one_dict("chl")
    ytd = sheng_one_dict("td")
    shengsi_data = merge_inv(ad, xlt, ytd,  ydo, yph, ychl,  ysal, ywt)
    return shengsi_data


def comp():
    ad = comp_one_dict("ad")
    xlt = comp_one_dict("lt")
    ydo = comp_one_dict("do")
    yph = comp_one_dict("ph")
    ywt = comp_one_dict("wt")
    ysal = comp_one_dict("sal")
    ychl = comp_one_dict("chl")
    ytd = comp_one_dict("td")
    comp_data = merge_inv(ad, xlt, ytd, ydo, yph, ychl, ysal,  ywt)
    return comp_data

if __name__ == '__main__':
    print(comp())


def tem_data(self, data):
    temperature_int = self.transform_binary(data[16:24])
    temperature_decimal = self.transform_binary(data[24:32])
    check_int = self.transform_binary(data[32:40])

