import urllib
import urllib2
import HTMLParser
from bs4 import BeautifulSoup
import re
import MySQLdb as mdb
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# --------------set userAgent, if not, the info maybe wrong----------------------#
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
)
cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = True
cap["phantomjs.page.settings.disk-cache"] = True
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
# )
driver = webdriver.PhantomJS(executable_path='/usr/local/src/phantomjs/bin/phantomjs', desired_capabilities=dcap)
# ------------------------------end----------------------------------------------#
#                                                                               #
# ---------------------Get company's name----------------------------------------#
i = 0
url = 'http://www.hnice.cn/service4.html'
request = urllib2.Request(url)
html = urllib2.urlopen(request)
soup = BeautifulSoup(html, 'lxml')
co_orig_names = soup.find_all(name='li', attrs={'class': 'st1'})
for co_orig_name in co_orig_names:
    if i == 0:
        i += 1
        continue
    print
    i
    print
    co_orig_name.string
    # ---------------------------------- end-----------------------------------------#
    #                                                                               #
    # ---------------------Get the company's info_url from search_url----------------#
    # chinese characters urlEncode
    co_orig_name = co_orig_name.string
    co_orig_name_1 = co_orig_name.encode('utf-8')
    name = {'key': co_orig_name_1}
    keyword = urllib.urlencode(name)
    url = 'http://www.tianyancha.com/search?' + keyword + '&searchType=company&checkFrom=searchBox'
    print
    url
    driver.get(url)
    # waiting the page loading completely   (wait the json turn to html)
    time.sleep(10)

    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'lxml')
    links = soup.find(name='a', attrs={'href': re.compile(r'^http://www.tianyancha.com/company/[0-9]*')})
    co_url = links.get('href')
    print
    co_url
    # -----------------------------------end-----------------------------------------#
    #
    # --------------open the company's info website and get info---------------------#
    driver.get(co_url)
    time.sleep(10)
    content = driver.page_source.encode('utf-8')
    # close browse
    # driver.close()
    # use bs4 to find a company's info
    soup = BeautifulSoup(content, 'lxml')
    co_names = soup.find(name='span', attrs={'class': re.compile(r'^f18 in-block vertival-middle ng-binding')})
    co_name = co_names.string
    co_tels = soup.find_all(name='span', attrs={'class': re.compile(r'^ng-binding')})
    # for co_tel in co_tels:
    co_tel = co_tels[1].string
    co_emails = soup.find(name='span',
                          attrs={'class': re.compile(r'^in-block vertical-top overflow-width emailWidth ng-binding')})
    co_email = co_emails.string
    co_addrs = soup.find(name='span',
                         attrs={'class': re.compile(r'^in-block overflow-width vertical-top emailWidth ng-binding')})
    co_addr = co_addrs.string
    print
    co_name
    print
    co_tel
    print
    co_email
    print
    co_addr
    # ------------------------------------end-----------------------------------------#
    #                                                                                #
    # ------------------------------------save in mysql-------------------------------#
    conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='password', db='tianyancha', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("insert into co_info values('%d','%s','%s','%s','%s','%s')" % (
    i, co_name, co_orig_name, co_tel, co_email, co_addr))
    cursor.close()
    conn.commit()
    conn.close()
    # -------------------------------------end----------------------------------------#
    time.sleep(10)
    i += 1