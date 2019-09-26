#coding:utf-8

import binascii
from src.radtest import truns



def test_transform_ip():
    """Check transforming ip for radius server format"""
    address1 = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, '192.168.1.1'.split('.')))
    address2 = truns('192.168.1.1')
    assert address1 == address2
