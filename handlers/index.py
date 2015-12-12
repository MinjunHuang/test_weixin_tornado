#coding:utf-8

import tornado.web
from model.entity import Entity

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        entity = Entity.get('ryan\'s blog')
        self.render('index.html', entity = entity)
