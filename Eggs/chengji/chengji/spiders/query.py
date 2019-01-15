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
        print(viewState)
        yield scrapy.FormRequest(url=url, callback=self.parse2, formdata={'__VIEWSTATE': 'dDwyMTQxMjc4NDIxOztsPF9jdGwwOkltYWdlQnV0dG9uMTtfY3RsMDpJbWFnZUJ1dHRvbjI7Pj4k81flOCblpdLMrVwk7oAsLQ+YHg==',
                                                                          '_ctl0:txtusername': response.meta['username'],
                                                                          '_ctl0:ImageButton1.x': '0',
                                                                          '_ctl0:ImageButton1.y': '0',
                                                                          '_ctl0:txtpassword': response.meta['password']})

    def parse1(self, response):
        url = 'http://yjsc.njue.edu.cn:8080/pyxx/leftmenu.aspx'
        print('redirect to leftMenu .....')
        print(response.request.headers.getlist('Cookie'))
        with open("save1.html", 'w', encoding='GBK') as f:
            f.write(response.text)
            f.close()
        yield scrapy.Request(url=url, callback=self.parse2, cookies={'ASP.NET_SessionId': 'poknxb55if5pl4552iivjkzu'})

    def parse2(self, response):
        Cookie2 = response.request.headers.getlist('Cookie')
        cookie = str(Cookie2[0]).replace('b', '').replace('\'', '').split('=')
        print(cookie[0])
        print(cookie[1])
        url2 = 'http://yjsc.njue.edu.cn:8080/pyxx/grgl/xskccjcx.aspx'
        with open("save2.html", 'w', encoding='GBK') as f:
            f.write(response.text)
            f.close()
        yield scrapy.Request(url=url2, callback=self.parse3, cookies={'ASP.NET_SessionId': cookie[1]})

    def parse3(self, response):
        name = response.xpath('//span[@id = "lblxm"]')
        name = name.xpath('string(.)').extract()[0]
        print(name)
        with open("%s_成绩.html" % name, 'w', encoding='GBK') as f:
            f.write(response.text)
            f.close()
