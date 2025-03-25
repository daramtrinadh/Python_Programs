import pytest

#ASSERTIONS: Validating the condition as it equals to Actual output to the expected output.
def test_assert():
    result=1+1
    assert result==2,"Expected result is 2"

#Fixtures :Piece of code that runs and returns output every time before the execution of each testcase.
@pytest.fixture
def sample_function():
    result=100
    return result
def test_case_sum(sample_function):
    assert 50+50==sample_function,f"Expected Result is {sample_function}"
def test_case_subs(sample_function):
    assert 200-100==sample_function,f"Expected Result is {sample_function}"


@pytest.mark.xfail("Expected is 2")
def test_check():
    assert 1+1==3
@pytest.mark.skip("This function is in implementation stage")
def test_skipfun():
    print("Skipped")
@pytest.mark.tryfirst
def test_tryfirstfun():
    print("Tried first")