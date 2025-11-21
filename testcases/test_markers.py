import sys
import pytest

#Skip a test unconditionally
@pytest.mark.skip(reason="Feature not ready")
def test_feature1():
    assert True

#Skip test only if condition is true
@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_feature2():
    assert True

#Mark test as expected to fail
@pytest.mark.xfail(reason="Known bug")
def test_feature3():
    assert 1/0    #forcing a failure by causing an exception(ZeroDivisionError)



