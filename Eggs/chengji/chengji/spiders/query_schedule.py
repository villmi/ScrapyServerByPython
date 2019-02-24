import scrapy


class QuerySpider(scrapy.Spider):
    name = "query_schedule"

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
        yield scrapy.FormRequest(url=url, callback=self.parse1, formdata={'__VIEWSTATE': viewState,
                                                                          '_ctl0:txtusername': response.meta['username'],
                                                                          '_ctl0:ImageButton1.x': '0',
                                                                          '_ctl0:ImageButton1.y': '0',
                                                                          '_ctl0:txtpassword': response.meta['password']})

    def parse1(self, response):
        Cookie2 = response.request.headers.getlist('Cookie')
        cookie = str(Cookie2[0]).replace('b', '').replace('\'', '').split('=')
        print(cookie[0])
        print(cookie[1])
        url2 = 'http://yjsc.njue.edu.cn:8080/pyxx/pygl/kbcx_xs.aspx'
        with open("save2.html", 'w', encoding='GBK') as f:
            f.write(response.text)
            f.close()
        yield scrapy.Request(url=url2, callback=self.parse2, cookies={'ASP.NET_SessionId': cookie[1]}, headers={'Referer': 'http://yjsc.njue.edu.cn:8080/pyxx/leftmenu.aspx'})

    def parse2(self, response):
        Cookie2 = response.request.headers.getlist('Cookie')
        cookie = str(Cookie2[0]).replace('b', '').replace('\'', '').split('=')
        values = response.xpath('//select/option')
        url3 = 'http://yjsc.njue.edu.cn:8080/pyxx/pygl/kbcx_xs.aspx'
        print(len(values))
        #name = response.xpath('//span[@id = "lblxm"]')
        #name = name.xpath('string(.)').extract()[0]
        #print(name)
        # with open("课表.html", 'w', encoding='GBK') as f:
            # f.write(response.text)
            # f.close()
        viewState = response.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first()
        eventArgument = response.xpath('//input[@name="__EVENTARGUMENT"]/@value').extract_first()
        eventTarget = response.xpath('//input[@name="__EVENTTARGET"]/@value').extract_first()
        for index, value in enumerate(values):
            print(value.xpath('//option/@value').extract()[index])
            yield scrapy.FormRequest(url=url3, callback=self.parse3, cookies={'ASP.NET_SessionId': cookie[1]}, formdata={
                '__EVENTTARGET': eventTarget,
                '__EVENTARGUMENT': eventArgument,
                '__VIEWSTATE': viewState,
                'drpxq': value.xpath('//option/@value').extract()[index],
                'btnSearch.x': '24',
                'btnSearch.y': '16'
            }, meta={'value': value.xpath('//option/@value').extract()[index]})

    def parse3(self, response):
        value = response.meta['value']
        print("3:")
        print(value)
        with open('/Users/vill/Desktop/课表_%s.html' % value, 'w', encoding='GBK') as f:
            f.write(response.text)
            f.close()
