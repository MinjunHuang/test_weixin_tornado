#coding:utf-8

import tornado.web
import hashlib

import commands
import xml.etree.ElementTree as ET
import time

def checksignature(signature, timestamp, nonce):
    args = []
    args.append('ryanchen') ####这里输入你的Token
    args.append(timestamp)
    args.append(nonce)
    args.sort()
    mysig = hashlib.sha1(''.join(args)).hexdigest()
    return mysig == signature

class VerifyHandler(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        if checksignature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.write('fail')
    def post(self): #######简单接收和发送消息
        body = self.request.body
        data = ET.fromstring(body)
        tousername = data.find('ToUserName').text
        fromusername = data.find('FromUserName').text
        createtime = data.find('CreateTime').text
        msgtype = data.find('MsgType').text
        content = data.find('Content').text
        msgid = data.find('MsgId').text
        #print 'fromusername: %s' % fromusername
        #print 'tousername: %s' % tousername
        #print 'createtime: %s' % createtime
        #print 'msgtype: %s' % msgtype
        #print 'msgid: %s' % msgid
        if content.strip() in ('ls','pwd','w','uptime'):
            result = commands.getoutput(content)
        else:
            result = '不可以哦!!!'
        textTpl = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[%s]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>"""
        out = textTpl % (fromusername, tousername, str(int(time.time())), msgtype, result)
        self.write(out)

