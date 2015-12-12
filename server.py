#coding:utf-8

import tornado.ioloop
import sys
from app import app

PORT = '8080'
ADDR = '0.0.0.0'
if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = sys.argv[1]
    app.listen(PORT,address=ADDR)
    print 'Development server is running at http://127.0.0.1:%s/' % PORT
    print 'Quit the server with CONTROL-C'
    tornado.ioloop.IOLoop.instance().start()
