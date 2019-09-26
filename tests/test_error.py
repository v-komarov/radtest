#coding:utf-8


from src.radtest import index

def test_index():
    """Check func index """
    assert index("0000000000","0.0.0.0") == "Error"
