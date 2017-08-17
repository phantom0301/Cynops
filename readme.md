Cynops:一款基于Networkx和Nmap的内网拓扑感知可视化工具
=======================================

Cynops是一个基于Flask框架的在线Nmap扫描与扫描结果Networkx显示工具，是一个综合使用Flask、python-libnmap、python-networkx、jsnetworkx的练习项目。

Documentation
-------------
Cynops使用Flask Web框架编写，通过前端调用python-nmap进行内网扫描，扫描结果经过Networkx处理后，将序列化结果返回到前端的js中进行可视化显示。

admin/cat

![](https://github.com/phantom0301/Cynops/blob/master/1.jpg)

![](https://github.com/phantom0301/Cynops/blob/master/2.jpg)

![](https://github.com/phantom0301/Cynops/blob/master/3.jpg)

![](https://github.com/phantom0301/Cynops/blob/master/4.jpg)

Dependencies
------------
- Nmap
- Python 2.7
- Flask and it's plugn-in
- python-libnmap
- python-networkx
- jsnetworkx


