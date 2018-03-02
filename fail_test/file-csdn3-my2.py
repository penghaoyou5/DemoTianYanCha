# -*- coding: utf-8 -*-
import time
import sys
import urllib
import requests

"""
Request URL:https://www.tianyancha.com/search?key=%E8%93%9D%E6%B1%9B%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&checkFrom=searchBox
Request Method:GET
Status Code:200 OK
Remote Address:180.97.163.185:443
Referrer Policy:no-referrer-when-downgrade


Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.9
Cache-Control:no-cache
Connection:keep-alive
Cookie:jsid=SEM-BAIDU-CG-SY-001063; TYCID=284aafe0058611e8872dc55eb98f1c37; undefined=284aafe0058611e8872dc55eb98f1c37; ssuid=8167267020; RTYCID=64567ae8475142c8a761e9091014521a; aliyungf_tc=AQAAAI0efBziHQEAAkL+Z/B8RiRkCKHn; csrfToken=CbneRPlIiDoz7XYdWdvYtJrR; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1517293441,1519782410,1519794489; token=95f17d1a9dd14a6aa5715d2e0fbc3735; _utm=7f8706ab0f6b42b9b7038e9cbe5506a1; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUwMDMyNjUxMCIsImlhdCI6MTUxOTgxOTEwNSwiZXhwIjoxNTM1MzcxMTA1fQ.V9SPBzAcSvoXXylQnpC2_ILPg3QnzEosAuFQ5y7fRBNI7FumP8XtmqtymjBZCZP61R9wtSLSV5SVkJfNysmTPg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218500326510%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUwMDMyNjUxMCIsImlhdCI6MTUxOTgxOTEwNSwiZXhwIjoxNTM1MzcxMTA1fQ.V9SPBzAcSvoXXylQnpC2_ILPg3QnzEosAuFQ5y7fRBNI7FumP8XtmqtymjBZCZP61R9wtSLSV5SVkJfNysmTPg; OA=t3Xr7Fv6JQk0nRgXxQ1Pemt0csom9rH+q4ng/p1XnvreT8FOlE3Bhr7fnxm8Q4/QdULp57K8SRmoqzOfA2x6/lqoCPb1KZRUKBBga9ZoVGoJPASR3SuzBHYwh6Gh0ZqHqFTPHPHbe/3E5svBC7ulv7WEkA2R9Xxc4Nw6CLrtHrU=; _csrf_bk=c48e14ac7b6b0169cd6ad0295b69a1a1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1519819130; _csrf=T31GbqN3vJ2OhslVMCP4Bg==
Host:www.tianyancha.com
Pragma:no-cache
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36


key:蓝汛通信有限公司
checkFrom:searchBox

"""

def main():
    headers ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'zh-CN,zh;q=0.9',
             'Cache-Control':'no-cache',
             'Connection':'keep-alive',
             'Host':'www.tianyancha.com',
             'Pragma':'no-cache',
             'Upgrade-Insecure-Requests':'1',
             'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
             }
    cookies = {'jsid':'SEM-BAIDU-CG-SY-001063',
                'TYCID':'284aafe0058611e8872dc55eb98f1c37',
                'undefined':'284aafe0058611e8872dc55eb98f1c37',
                'ssuid':'8167267020',
                'RTYCID':'64567ae8475142c8a761e9091014521a',
                'aliyungf_tc':'AQAAAI0efBziHQEAAkL+Z/B8RiRkCKHn',
                'csrfToken':'CbneRPlIiDoz7XYdWdvYtJrR',
                'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1517293441,1519782410,1519794489',
                'token':'95f17d1a9dd14a6aa5715d2e0fbc3735',
                '_utm':'7f8706ab0f6b42b9b7038e9cbe5506a1',
                'tyc-user-info':'%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUwMDMyNjUxMCIsImlhdCI6MTUxOTgxOTEwNSwiZXhwIjoxNTM1MzcxMTA1fQ.V9SPBzAcSvoXXylQnpC2_ILPg3QnzEosAuFQ5y7fRBNI7FumP8XtmqtymjBZCZP61R9wtSLSV5SVkJfNysmTPg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218500326510%2522%257D',
                'auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUwMDMyNjUxMCIsImlhdCI6MTUxOTgxOTEwNSwiZXhwIjoxNTM1MzcxMTA1fQ.V9SPBzAcSvoXXylQnpC2_ILPg3QnzEosAuFQ5y7fRBNI7FumP8XtmqtymjBZCZP61R9wtSLSV5SVkJfNysmTPg',
                'OA':'t3Xr7Fv6JQk0nRgXxQ1Pemt0csom9rH+q4ng/p1XnvreT8FOlE3Bhr7fnxm8Q4/QdULp57K8SRmoqzOfA2x6/lqoCPb1KZRUKBBga9ZoVGoJPASR3SuzBHYwh6Gh0ZqHqFTPHPHbe/3E5svBC7ulv7WEkA2R9Xxc4Nw6CLrtHrU=',
                '_csrf_bk':'c48e14ac7b6b0169cd6ad0295b69a1a1',
                'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1519819130',
                '_csrf':'T31GbqN3vJ2OhslVMCP4Bg=='
             }
    keyword = '蓝汛通信有限公司'
    keyword  = '百度'
    startUrl = 'http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % urllib.quote(keyword)

    resultPage = requests.get(startUrl, headers=headers, cookies=cookies)  # 在请求中设定头，cookie

    time.sleep(10)

    with open('tyc_demo2.txt', 'w') as of:
        of.write(resultPage.text)
    get_basic_info(resultPage.text)


def get_basic_info(soup):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(soup, 'lxml')
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



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()