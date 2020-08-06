import pytest
from test_calc.calc import Calclator


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
    def test_jia(self):
        # calc = Calclator()
        result = self.calc.jia(1,2)
        print("1+2 = 3")
        assert 3 == result

    def test_jian(self):
        # calc = Calclator()
        result = self.calc.jian(2,1)
        print("2-1 = 1")
        assert 1 == result

    def test_cheng(self):
        # calc = Calclator()
        result = self.calc.cheng(1,2)
        print("1*2 = 2")
        assert 2 == result

    def test_chu(self):
        # calc = Calclator()
        result = self.calc.chu(2,1)
        print("2/1 = 2")
        assert 2 == result