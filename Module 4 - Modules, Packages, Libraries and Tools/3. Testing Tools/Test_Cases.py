import Test_Code
import pytest

def test_add():
    assert Test_Code.add(2,3) == 5
    assert Test_Code.add(-5,5) == 0

def test_sub():
    assert Test_Code.sub(2,3) == -1
    assert Test_Code.sub(3,2) == 1