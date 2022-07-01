import pytest

def test_1():
    num = 1 + 1
    assert num == 2, 'num==2条件不满足'

def test_2():
    num = 1 + 1
    assert  num == 3, 'num==3条件不满足'

if __name__ == '__main__':
    pytest.main(['-s'])
