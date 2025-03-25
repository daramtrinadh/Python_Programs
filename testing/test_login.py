import pytest
#
# @pytest.mark.trylast
# def test_add():
#     assert 2+4==6
#     print("Addition is worked")
# @pytest.mark.tryfirst
# def test_sub():
#     assert 3+4==7
#     print("Substarction")
@pytest.mark.tryfirst
def test_add(setup):
    assert 2+4==8
    print("Failed")
@pytest.fixture
def setup():
    print("Launch browser")
    print("Browser started")
    yield
    print("log off")
    print("close browser")
def test_additioncart(setup):
    print("Item is added")
def test_remove(setup):
    print("item is served succssfully")
