#coding:utf-8

import radius
import binascii
import bottle
from bottle import route, run, get
import conf

secret = conf.secret
server = conf.server


def truns(ip):
    ip = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, ip.split('.')))
    return ip


def check_radius(mac,address,server,secret):

    r = radius.Radius(secret, host=server)

    attrs = { 'Framed-IP-Address':binascii.unhexlify(address) }

    try:
        return r.authenticate(mac,mac, attributes=attrs)
    except:
        return 'Error'



@get('/<mac>/<ip>')
def index(mac,ip):
    address = truns(ip)
    return check_radius(mac,address,server,secret)


if __name__ == "__main__":
    run(host="localhost", port=8080)


app = bottle.default_app()
