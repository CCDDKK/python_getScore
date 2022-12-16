# python_getScore
python利用selenium爬取掌上高考网


## 使用Python模拟人点击浏览器 ，获取高考信息

在本地有python的前提， 还得有一个(浏览器driver.exe)， 如chromedriver.exe ,这就需要chrome浏览器（自行下载），压缩包里有chromedriver.exe  ，把它放到你本地python.exe的同级目录：
![1670661176064](https://github.com/ccddkk9/python_getScore/blob/main/img/1670661176064.png)
这样 放置。

谷歌浏览器版本要和chromedriver.exe 版本接近就行，要是不一样 百度去搜索chromedriver下载就好。chromedriver的链接：
https://chromedriver.chromium.org/downloads

下面是我的版本。如果是这个版本的浏览器 ，可以用我给的chromedriver.exe 如果不是更新下浏览器就行。
![1670661948106](https://github.com/ccddkk9/python_getScore/blob/main/img/1670661948106.png)

准备好后python需要安装几个库  selenium  、 sqlalchemy    、 pandas 用pip安装好！

提供了sql文件 把表创建好！

然后你就可以运行压缩包里的.py文件了 ，记得把第七行改成你自己的数据库名和密码！

还有一件事，运行程序后不要用鼠标点击了！

