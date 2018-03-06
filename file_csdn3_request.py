# -*- coding: utf-8 -*-
import time
import sys
import urllib
import requests
import file_csdn3_util

"""
一个账号只能查询100条，所以应该需要多个账号的源进行轮流查询


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
import os
def main(keyword):
    file_name  = "tyc_demo2.txt"

    if os.path.exists(file_name):
        os.remove(file_name)


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

    startUrl = 'http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % keyword # urllib.quote(keyword)

    resultPage = requests.get(startUrl, headers=headers, cookies=cookies)  # 在请求中设定头，cookie

    time.sleep(10)

    with open(file_name, 'w') as of:
        of.write(resultPage.text)


def main_while(keyword):
    get_result = False
    while not get_result:
        try:
            main(keyword)
            get_result = True
        except Exception as e:
            file_csdn3_util.write_error(e)
            print e


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    keyword = '蓝汛通信有限公司'
    keyword  = '百度'
    main(keyword)