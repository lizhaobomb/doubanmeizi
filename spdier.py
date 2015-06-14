# -*- coding:utf8 -*-
# 抓取dbmei.com的图片。

from bs4 import BeautifulSoup
import os, sys, urllib2

reload(sys)
sys.setdefaultencoding("utf-8")

# 创建文件夹，昨天刚学会
path = os.getcwd()                           # 获取此脚本所在目录
new_path = os.path.join(path,u'豆瓣妹子')
if not os.path.isdir(new_path):
    os.mkdir(new_path)

def page_loop(page=1):
    url = 'http://www.dbmeinv.com/dbgroup/rank.htm?pager_offset=%s' % page
    content = urllib2.urlopen(url)

    soup = BeautifulSoup(content)

    my_girl = soup.find_all('img')   
    # 加入结束检测，写的不好....
    if my_girl ==[]:
        print u'已经全部抓取完毕'
        sys.exit(0)

    print u'开始抓取'
    for girl in my_girl:
        link = girl.get('src')
        # flink = 'http://www.dbmeizi.com/' + link

        print link
        content2 = urllib2.urlopen(link).read()
        with open(u'豆瓣妹子'+'/'+link[-11:],'wb') as code:   #在OSC上现学的
            code.write(content2)
    page = int(page) + 1
    print u'开始抓取下一页'
    print 'the %s page' % page
    page_loop(page)

page_loop()
