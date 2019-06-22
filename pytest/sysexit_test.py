import pytest

def f():
    raise SystemExit(1)

# mytest_test(): did not worked in pytest3.10.1
def test_mytest():
    with pytest.raises(SystemExit):f()
