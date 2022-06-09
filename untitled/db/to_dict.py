from db.db_query import Tao, Sheng, Dong, Comp_data
# from db.util import dict_to_json


def tao_one_dict(field):
    '''第一个参数为返回的数值，第二个参数为查询数据库中的字段名'''
    dict_data = {}
    tao = Tao()
    inner = []
    for data in tao.tao_data(f"{field}"):
        inner.append(data[0])
    dict_data[f"{field}"] = inner
    return dict_data


def dong_one_dict(field):
    '''第一个参数为返回的数值，第二个参数为查询数据库中的字段名'''
    dict_data = {}
    dong = Dong()
    inner = []
    for data in dong.dong_data(f"{field}"):
        inner.append(data[0])
    dict_data[f"{field}"] = inner
    return dict_data



def sheng_one_dict(field):
    '''第一个参数为返回的数值，第二个参数为查询数据库中的字段名'''
    dict_data = {}
    sheng = Sheng()
    inner = []
    for data in sheng.sheng_data(f"{field}"):
        inner.append(data[0])
    dict_data[f"{field}"] = inner
    return dict_data

# 需要两个参数，一个存放监测地点，一个存放监测数据
def comp_one_dict(field):
    dict_data = {}
    comp = Comp_data()
    inner = []
    for data in comp.comp_data(f"{field}"):
        inner.append(data[0])
    dict_data[f"{field}"] = inner
    return dict_data


if __name__ == '__main__':
    pass
    # yco2 = tao_one_dict("co2")
    # n = tao_one_dict("n")
    # xptime = tao_one_dict("ptime")
    # a = dict_to_json(n)
    # print(a)
    # merge_dict = merge(xptime, yco2)
    # xy_axis = dict_to_json(merge_dict)
    # print(xy_axis)
    #{"co2": [5.36, 6.36, 7.36, 8.36, 9.36, 10.36, 11.36, 12.36, 13.36, 14.36, 15.36, 16.36, 17.36, 18.36, 19.36, 20.36, 21.36, 22.36, 5.36, 6.36, 7.36, 8.36, 9.36, 10.36, 11.36, 12.36, 13.36, 14.36, 15.36, 16.36, 17.36, 18.36, 19.36, 20.36, 21.36, 22.36]}
