# ScrapyServerByPython
## it's the final project for 毛波
<br>

***于2019.2.24--关于大作业***<br>
在开学的最后一天将程序更新了，因为老家没有网的缘故所以只在本地git了并没有更新github。<br>
如果用于检查作业，这个项目中的彩蛋部分应该是比较好检验的一部分，即Eggs，其中包含两个爬虫：<br>
*   *成绩查询--query_chenji（我知道成是后鼻音～～～）*
*   *课表查询--query_schedule*<br>
通过之前我写的说明可以使用本程序快速爬去研究生系统里的个人的所有已存在的课表以及成绩单并存放在程序根目录里，之前的内容也介绍了用于我个人mac的shell脚本.<br>
为了方便检查作业以及环境不匹配已经录制了一个视频，如果有时间老师可以观看，感觉效果还行,是基于我自己的电脑的<br>
具体代码是<a href="https://github.com/villmi/ScrapyServerByPython/tree/demo" target="_blank">demo</a>分支（单纯只是改了文件位置）<br>
<a href="http://v.youku.com/v_show/id_XNDA3Njk4NzU5Mg==.html?spm=a2hzp.8244740.0.0" target="_blank">我是视频，可以点的</a>



***于2019.1.24--关于Eggs***<br>
这个项目的名字叫彩蛋，缘由是出于算法导论因为一些个人原因要<a href="https://baike.baidu.com/item/挂科/728747?fr=aladdin">挂科</a>（结果真的挂了，不过只能接受了，难不成退学吗？），就写了一个程序可以去爬教务系统中成绩的程序，操作是繁琐一点了<br>
使用的格式是 *scrapy crawl query_chenji -a keyword=学号,密码*<br>
不过因为本人使用的系统是OSX所以编写一个shell，只要双击就可以成绩很快地以html的格式放到桌面上，local分支即是个人使用的版本<br>
shell就长下面这样（对，就是这么简单）<br>
![1111](https://raw.githubusercontent.com/villmi/ScrapyServerByPython/master/img/shell-img.png)<br>
之后我还加入了一个查询课表的爬虫，叫做query_schedule，使用方法参照上面一个<br>





