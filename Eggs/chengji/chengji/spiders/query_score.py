import scrapy


class QuerySpider(scrapy.Spider):
    name = "query_chenji"

    def start_requests(self):
        url = 'http://210.28.80.133:8080/pyxx/login.aspx'
        tag = getattr(self, 'keyword', None)
        tag = str(tag).split(',')
        username = tag[0]
        password = tag[1]
        yield scrapy.Request(url=url, callback=self.parse, meta={'username': username, 'password': password})

    def parse(self, response):
        url = 'http://210.28.80.133:8080/pyxx/login.aspx'
        viewState = response.xpath('/html/body/form/input[@name="__VIEWSTATE"]/@value').extract_first()

        yield scrapy.FormRequest(url=url, callback=self.parse1, formdata={'__VIEWSTATE': viewState,
                                                                          '_ctl0:txtusername': response.meta['username'],
                                                                          '_ctl0:ImageButton1.x': '0',
                                                                          '_ctl0:ImageButton1.y': '0',
                                                                          '_ctl0:txtpassword': response.meta['password']},
                                 meta={'username': response.meta['username'], 'password': response.meta['password']})

    def parse1(self, response):
        Cookie2 = response.request.headers.getlist('Cookie')
        cookie = str(Cookie2[0]).replace('b', '').replace('\'', '').split('=')
        url2 = 'http://yjsc.njue.edu.cn:8080/pyxx/grgl/xskccjcx.aspx'
        with open("save2.html", 'w', encoding='GBK') as f:
            f.write(response.text)
            f.close()
        yield scrapy.Request(url=url2, callback=self.parse2, cookies={'ASP.NET_SessionId': cookie[1]},
                             meta={'username': response.meta['username'], 'password': response.meta['password']})

    def parse2(self, response):
        name = response.xpath('//span[@id = "lblxm"]')
        try:
            name = name.xpath('string(.)').extract()[0]
            with open("%s_成绩.html" % name, 'w', encoding='GBK') as f:
                f.write(response.text)
                f.close()
        except:
            print('failed')
            Cookie = response.request.headers.getlist('Cookie')
            print(Cookie)
            url = 'http://210.28.80.133:8080/pyxx/login.aspx'
            yield scrapy.Request(url=url, callback=self.parse, meta={'username': response.meta['username'], 'password': response.meta['password']})








