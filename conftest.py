import pytest
import yaml
from test_calc.calc import Calclator

with open('C:\\Users\zhangcaiju_v\PycharmProjects\learning\Project\\test_calc\datas.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)['datas']
    jia_datas = datas['jia_datas']
    jian_datas = datas['jian_datas']
    cheng_datas = datas['cheng_datas']
    chu_datas = datas['chu_datas']
    myid = datas['myid']

@pytest.fixture(scope='module')
def get_clac():
    print('开始计算')
    calc = Calclator()
    yield calc
    print('结束计算')

@pytest.fixture(scope='function',params=jia_datas, ids=myid)
def get_jia_param(request):
    print(f'此处传入的参数是：{request.param}')
    yield request.param

@pytest.fixture(scope='function', params=jian_datas, ids=myid)
def get_jian_param(request):
    yield request.param

@pytest.fixture(scope='function', params=cheng_datas, ids=myid)
def get_cheng_param(request):
    yield request.param

@pytest.fixture(scope='function', params=chu_datas, ids=myid)
def get_chu_param(request):
    yield request.param