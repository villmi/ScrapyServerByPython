import sqlite3
import socketserver
import json


class Server(socketserver.BaseRequestHandler):
    def handle(self):
        terminal = False
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        while not terminal:
            request = str(self.request.recv(1024), 'utf8')
            print('the msg is %s' % request)
            if request is not None:
                request = json.loads(request)
                keywords = request['keywords']
                count = int(request['count'])
                length = len(str(keywords).split(','))

                keyword = ''
                for key in keywords:
                    keyword += keywords[key]
                    keyword += ' '
                cursor.execute("select * from query where word=\'%s\'" % keyword)
                if cursor.fetchone():
                    pass





