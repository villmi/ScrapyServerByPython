# ScrapyServerByPython
it's the final project for maobo
<br>

***于2019.1.24--关于Eggs***<br>
这个项目的名字叫彩蛋，缘由是出于算法导论因为一些个人原因要挂科（结果真的挂了，不过只能接受了，难不成退学吗？），就写了一个程序可以去爬教务系统中成绩的程序，操作是繁琐一点了<br>
使用的格式是 **italic**scrapy crawl query_chenji -a keyword=学号,密码<br>
不过因为本人使用的系统是OSX所以编写一个shell，只要双击就可以成绩很快地以html的格式放到桌面上，local分支是个人使用的<br>
shell就长下面这样（对，就是这么简单）<br>
![1111](https://raw.githubusercontent.com/villmi/ScrapyServerByPython/master/img/shell-img.png)<br>
之后我还加入了一个查询课表的爬虫，叫做uery_schedule，使用方法参照上面一个，毕竟好久没有写代码了，写这两个基于Scrapy的爬虫练练手。
