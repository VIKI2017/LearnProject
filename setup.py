
import pytest
#setup和teardown运用

class Testceshi:
    def SetUp(self):
        print("开始计算-----")

    def TearDown(self):
        print("结束计算-----------")

    @pytest.mark.parametrize('a,b', [(1, 2), (2, 4)])
    def test_add(self,a, b):
        try:
            print("结果是：", a + b)
        except TypeError:
            print("参数类型有误")

    @pytest.mark.parametrize('a,b', [(3, 6), (3, 9)])
    def test_div(self,a, b):
        try:
            result = a / b
            assert result == 0.5
            print("结果是：", result)
        except ZeroDivisionError:
            print("分母不能为0")
            return 0
        except TypeError:
            print("参数类型有误")
