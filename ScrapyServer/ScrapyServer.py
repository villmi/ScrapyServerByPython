import sqlite3
import socketserver
import json
import threading
import time
import os


class Server(socketserver.BaseRequestHandler):
    def handle(self):
        # some object
        response = {}
        i = 1
        over = False# 数据库查询结果是否返回完全
        terminal = False# 返回数据的过程是否结束
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        while not terminal:
            request = str(self.request.recv(1024), 'utf8')
            print('the msg is %s' % request)
            if request is not None:
                request = json.loads(request)
                keywords = request['keywords']
                count = int(request['count'])# 一开始协议中使用的参数，仅用于java，length同理，此程序中应该用不到
                length = len(str(keywords).split(','))

                keyword = ''
                for key in keywords:
                    keyword += keywords[key]
                    keyword += ' '
                cursor.execute("select * from query where word=\'%s\'" % keyword)
                result = cursor.fetchone()
                if result is not None:
                    while not over:
                        if result is None:
                            over = True
                        else:
                            response['$s' % i] = {'title': result[0],
                                                  'url': result[1],
                                                  'location': result[2],
                                                  'channel': result[3],
                                                  'pubdate': result[4]}
                            i += 1
                            result = cursor.fetchone()
                    response = json.dumps({'head': 'villhahahaha',
                                           'description': 'scrapy_result',
                                           'result': response,
                                           'end': 'end'})
                    self.request.sendall(response)
                else:
                    command = './scrapy.sh %s,%s' % (keyword, count)

                    def action(cmd):
                        a = os.popen(cmd)
                        a.read()
                    threading.Thread(target=action, args=command)
                    while not over:
                        time.sleep(1)
                        sql = "select * from spider.query where word='%s'" % keyword
                        cursor.execute(sql)
                        state = cursor.fetchone()
                        if state is not None:
                            state = state[3]
                        if state == 1:
                            over = True
                            sql = "select * from spider.query where word='%s'" % keyword
                            cursor.execute(sql)
                            tableName = cursor.fetchone()
                            if tableName is not None:
                                tableName = tableName[2]
                            sql = "select * from spider.`%s`" % tableName
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            if result is not None:
                                while not over:
                                    if result is None:
                                        over = True
                                    else:
                                        response['$s' % i] = {'title': result[0],
                                                              'url': result[1],
                                                              'location': result[2],
                                                              'channel': result[3],
                                                              'pubdate': result[4]}
                                        i += 1
                                        result = cursor.fetchone()
                                response = json.dumps({'head': 'villhahahaha',
                                                       'description': 'scrapy_result',
                                                       'result': response,
                                                       'end': 'heiheihei'})
                                self.request.sendall(response)
                        else:
                            over = False























