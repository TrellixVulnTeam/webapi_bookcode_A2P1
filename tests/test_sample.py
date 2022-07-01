import pytest
@pytest.fixture
def app_data():
    return 3

def test_func3(app_data):
    assert app_data == 3

def test_func2():
    assert 2==2

def test_01():
    print("我是test_01")

def test_02():
    print("我是test_02")

class Test_demo(object):

    def test_03(self):
        print("我是test_03")

    def test_04(self):
        print("我是test_04")

class Tsts_demo(object):
    def test_05(self):
        print("我是test_05")


if __name__ == '__main__':
    pytest.main(['-s'])
