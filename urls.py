#coding:utf-8
from handlers.index import MainHandler
from handlers.verify import VerifyHandler

urls = [
    (r'/', MainHandler),
    (r'/verify', VerifyHandler),
]
