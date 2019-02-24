# ScrapyServerByPython
## it's the final project for 毛波
<br>
***于2019.2.24--关于大作业***<br>
在开学的最后一天将程序更新了，因为老家没有网的缘故所以只在本地git了并没有更新github。<br>
如果用于检查作业，这个项目中的彩蛋部分应该是比较好检验的一部分，即Eggs，其中包含两个爬虫：<br>
*   *成绩查询*
*   *课表查询*
通过下面内容可以使用本程序快速爬去研究生系统里的个人的所有已存在的课表以及成绩单并存放在程序根目录里，之前的内容也介绍了，用于我个人mac的shell脚本.<br>

***于2019.1.24--关于Eggs***<br>
终于调通了C/S结构了，接下来可以改写kotlin代码了<br>
调了半天想要完善Client代码可是发现我这次要写的主要部分是Server，本末倒置了，可能寒假就是用来浪费的吧<br>

***于2019.1.24--关于Eggs***<br>
这个项目的名字叫彩蛋，缘由是出于算法导论因为一些个人原因要挂科（结果真的挂了，不过只能接受了，难不成退学吗？），就写了一个程序可以去爬教务系统中成绩的程序，操作是繁琐一点了<br>
使用的格式是 *scrapy crawl query_chenji -a keyword=学号,密码*<br>
不过因为本人使用的系统是OSX所以编写一个shell，只要双击就可以成绩很快地以html的格式放到桌面上，local分支即是个人使用的版本<br>
shell就长下面这样（对，就是这么简单）<br>
![1111](https://raw.githubusercontent.com/villmi/ScrapyServerByPython/master/img/shell-img.png)<br>
之后我还加入了一个查询课表的爬虫，叫做query_schedule，使用方法参照上面一个，毕竟好久没有写代码了，写这两个基于Scrapy的爬虫练练手。<br>

***于2019.1.24--关于这个项目***<br>
终于开始准备这次的python大作业了。<br>
之前帮导师写了一个爬虫去爬一个网站的数据所以我分别编写了基于Scrapy的爬虫，Android APP以及一个服务器程序,因为寒假好像事情点多（对，我<a href="https://baike.baidu.com/item/挂科/728747?fr=aladdin">挂科</a>了），所以打算把之前项目中的服务器程序用python写一遍，顺带一提，之前服务器程序是用<a href="http://kotlinlang.org">kotlin</a>（我曾以为跟着谷歌能征服世界）编写的。<br>
然后因为对于成绩的渴望编写了一个彩蛋，以下我应该会作介绍。<br>
言归正传，稍微介绍一下服务器的功能,主要如下：<br>
*   *监听客户端请求*
*   *根据请求查询数据库或调用爬虫*
*   *向客户端返回数据*
功能暂时就这么多，图书馆要下班了，我先溜了。。。。。


