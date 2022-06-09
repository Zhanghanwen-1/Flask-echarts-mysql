from flask import Flask
from flask import render_template
from db.util import dict_to_json, taohua, dongji, shengsi,comp

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# 对比图需要获取的数据为每个监测点的数据

@app.route('/comp', methods=['POST', 'GET'])
def index_comp():
    axis_value = dict_to_json(comp())
    return (axis_value)


@app.route('/Dong')
def dong():
    axis_value = dict_to_json(dongji())
    return (axis_value)


@app.route('/Tao')
def index_tao():
    axis_value = dict_to_json(taohua())
    return (axis_value)

@app.route('/Sheng')
def sheng():
    axis_value = dict_to_json(shengsi())
    return (axis_value)

if __name__ == '__main__':
    app.run()
