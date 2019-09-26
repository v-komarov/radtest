#coding:utf-8

import os
import pytest
from src.conf import server, secret


def test_radius_host():
    """Check reading radius host"""
    assert server == "127.0.0.1"


def test_radius_secret():
    """Check reading radius secret"""
    assert secret == "xxx"
