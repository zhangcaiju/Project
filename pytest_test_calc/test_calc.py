import pytest
import yaml
from test_calc.calc import Calclator

with open('C:\\Users\zhangcaiju_v\PycharmProjects\learning\Project\\test_calc\datas.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)['datas']
    add_datas = datas['jia_datas']
    jian_datas = datas['jian_datas']
    cheng_datas = datas['cheng_datas']
    chu_datas = datas['chu_datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


class TestCalc:

    def setup_class(self):
        print("类级别开始")
        self.calc = Calclator()

    def teardown_class(self):
        print("类级别结束")

    def setup(self):
        print("开始测试")

    def teardown(self):
        print("测试结束")

    @pytest.mark.jia
    @pytest.mark.parametrize('a,b,excepted', add_datas, ids=myid)
    def test_jia(self, a, b, excepted):
        # calc = Calclator()
        result = self.calc.jia(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        print("加法计算")
        assert excepted == result

    @pytest.mark.parametrize('a,b,excepted', jian_datas, ids=myid)
    def test_jian(self, a, b, excepted):
        # calc = Calclator()
        result = self.calc.jian(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        print("减法计算")
        assert excepted == result

    @pytest.mark.parametrize('a,b,excepted', cheng_datas, ids=myid)
    def test_cheng(self, a, b, excepted):
        # calc = Calclator()
        result = self.calc.cheng(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        print("乘法计算")
        assert excepted == result

    @pytest.mark.parametrize('a,b,excepted', chu_datas, ids=myid)
    def test_chu(self, a, b, excepted):
        # calc = Calclator()
        result = self.calc.chu(a, b)
        print("除法计算")
        assert excepted == result
