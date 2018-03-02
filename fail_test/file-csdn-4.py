#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def driver_open():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    )
    driver = webdriver.PhantomJS(executable_path='/Users/penghaoyou/Documents/phantomjs-2.1.1-macosx/bin/phantomjs', desired_capabilities=dcap)
    return driver
def get_content(driver,url):
    driver.get(url)
#等待5秒，更据动态网页加载耗时自定义
    time.sleep(5)
# 获取网页内容
    content = driver.page_source.encode('utf-8')
    driver.close()
    soup = BeautifulSoup(content, 'lxml')
    return soup

def get_basic_info(soup):
    company = soup.select('div.company_info_text > p.ng-binding')[0].text.replace("\n","").replace(" ","")
    fddbr = soup.select('.td-legalPersonName-value > p > a')[0].text
    zczb = soup.select('.td-regCapital-value > p ')[0].text
    zt = soup.select('.td-regStatus-value > p ')[0].text.replace("\n","").replace(" ","")
    zcrq = soup.select('.td-regTime-value > p ')[0].text
    basics = soup.select('.basic-td > .c8 > .ng-binding ')
    hy = basics[0].text
    qyzch = basics[1].text
    qylx = basics[2].text
    zzjgdm = basics[3].text
    yyqx = basics[4].text
    djjg = basics[5].text
    hzrq = basics[6].text
    tyshxydm = basics[7].text
    zcdz = basics[8].text
    jyfw = basics[9].text
    print u'公司名称：'+company
    print u'法定代表人：'+fddbr
    print u'注册资本：'+zczb
    print u'公司状态：'+zt
    print u'注册日期：'+zcrq
    # print basics
    print u'行业：'+hy
    print u'工商注册号：'+qyzch
    print u'企业类型：'+qylx
    print u'组织机构代码：'+zzjgdm
    print u'营业期限：'+yyqx
    print u'登记机构：'+djjg
    print u'核准日期：'+hzrq
    print u'统一社会信用代码：'+tyshxydm
    print u'注册地址：'+zcdz
    print u'经营范围：'+jyfw

def get_gg_info(soup):
    ggpersons = soup.find_all(attrs={"event-name": "company-detail-staff"})
    ggnames = soup.select('table.staff-table > tbody > tr > td.ng-scope > span.ng-binding')
    # print(len(gg))
    for i in range(len(ggpersons)):
            ggperson = ggpersons[i].text
            ggname = ggnames[i].text
    print (ggperson+" "+ggname)

def get_gd_info(soup):
    tzfs = soup.find_all(attrs={"event-name": "company-detail-investment"})
    for i in range(len(tzfs)):
            tzf_split = tzfs[i].text.replace("\n","").split()
            tzf = ' '.join(tzf_split)
    print tzf

def get_tz_info(soup):
    btzs = soup.select('a.query_name')
    for i in range(len(btzs)):
            btz_name = btzs[i].select('span')[0].text
    print btz_name

if __name__=='__main__':
    url = "http://www.tianyancha.com/company/2310290454"
    driver = driver_open()
    soup = get_content(driver, url)
    print soup
    print '----获取基础信息----'
    get_basic_info(soup)
    print '----获取高管信息----'
    get_gg_info(soup)
    print '----获取股东信息----'
    get_gd_info(soup)
    print '----获取对外投资信息----'
    get_tz_info(soup)