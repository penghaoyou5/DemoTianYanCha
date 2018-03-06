这两天离职在家，跟朋友帮了个小忙，写了个脚本拉取天眼查公司数据

因为也需求就400条请求所以写了这么简单  个人账户登录就可以请求100条 所以没必要写太复杂了

运行  python file_csdn3_main.py
里面有参数 现在是读取1到10行的数据（source.xls中的公司名）  结果写入 result.xls中，当然参数可以改变


因为request中用的是本人的 request_head 有可能失败，只要抓包换成自己账户登录的 请求头 即可（因为每个账户有查询限制）

fail_test是尝试过网上的失败案例，因为自己实现这个功能就行  就没写复杂了


pypenghaoyoudeMBP:MyPhanjs penghaoyou$ python -V
Python 2.7.10


xlrd (1.1.0)
XlsxWriter (1.0.2)
bs64 4.6.0
urllib (1.21.1)
requests (2.18.4)
sudo pip install xlutils;
