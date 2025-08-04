from src.utils import return_hexadecimal

def test_hex():
    assert return_hexadecimal(10) == "0xa"
