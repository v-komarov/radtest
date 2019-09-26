#coding:utf-8

import os


server = os.environ.get("RADIUS_HOST", "127.0.0.1") # Address of radius server
secret = os.environ.get("RADIUS_SECRET", "xxx") # Secret of radius server
 