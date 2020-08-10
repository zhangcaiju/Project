# import pytest
# import yaml
# from test_calc.calc import Calclator
#
# with open('C:\\Users\zhangcaiju_v\PycharmProjects\learning\Project\\test_calc\datas.yml', encoding='utf-8') as f:
#     datas = yaml.safe_load(f)['datas']
#     jia_datas = datas['jia_datas']
#     jian_datas = datas['jian_datas']
#     cheng_datas = datas['cheng_datas']
#     chu_datas = datas['chu_datas']
#     myid = datas['myid']
#
# @pytest.fixture(scope='module')
# def get_clac():
#     calc = Calclator()
#     yield calc
#
# @pytest.fixture(scope='function',params=jia_datas, ids=myid)
# def get_jia_param(request):
#     print(f'此处传入的参数是：{request.param}')
#     yield request.param
#
# @pytest.fixture(scope='function', params=jian_datas, ids=myid)
# def get_jian_param(request):
#     yield request.param
#
# @pytest.fixture(scope='function', params=cheng_datas, ids=myid)
# def get_cheng_param(request):
#     yield request.param
#
# @pytest.fixture(scope='function', params=chu_datas, ids=myid)
# def get_chu_param(request):
#     yield request.param


class TestCalc:

    # def setup_class(self):
    #     print("类级别开始")
    #     self.calc = Calclator()
    #
    # def teardown_class(self):
    #     print("类级别结束")
    #
    # def setup(self):
    #     print("开始测试")
    #
    # def teardown(self):
    #     print("测试结束")

    # @pytest.mark.jia
    # @pytest.mark.parametrize('a,b,excepted', add_datas, ids=myid)
    def test_jia(self,get_clac, get_jia_param):
        # calc = Calclator()
        result = get_clac.jia(get_jia_param[0], get_jia_param[1])
        if isinstance(result, float):
            result = round(result, 2)
        print("加法计算")
        assert get_jia_param[2] == result

    # @pytest.mark.parametrize('a,b,excepted', jian_datas, ids=myid)
    def test_jian(self, get_clac, get_jian_param):
        # calc = Calclator()
        result = get_clac.jian(get_jian_param[0], get_jian_param[1])
        if isinstance(result, float):
            result = round(result, 2)
        print("减法计算")
        assert get_jian_param[2] == result

    # @pytest.mark.parametrize('a,b,excepted', cheng_datas, ids=myid)
    def test_cheng(self, get_clac, get_cheng_param):
        # calc = Calclator()
        result = get_clac.cheng(get_cheng_param[0], get_cheng_param[1])
        if isinstance(result, float):
            result = round(result, 2)
        print("乘法计算")
        assert get_cheng_param[2] == result

    # @pytest.mark.parametrize('a,b,excepted', chu_datas, ids=myid)
    def test_chu(self, get_clac, get_chu_param):
        # calc = Calclator()
        result = get_clac.chu(get_chu_param[0], get_chu_param[1])
        print("除法计算")
        assert get_chu_param[2] == result
