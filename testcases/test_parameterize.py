import pytest

@pytest.mark.parametrize("name", ["subha"])
def test_validation(name):
    assert name!= None


@pytest.mark.parametrize("name,role",[("subha","analyst"),("madhu","architecht")])
def test_validation2(name,role):
    assert name!= None
    assert role!= None

@pytest.fixture(scope="module", params=["www.google.com","www.amazon.com"])
def setup(request):
    return request.param

def test_val(setup):
    assert setup!= None
