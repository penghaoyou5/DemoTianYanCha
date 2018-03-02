from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
import urllib

#获取企业基本信息数据
def get_enterprise_data(ename):
    #搜索页面链接地址
    keyword = urllib.parse.quote(ename)
    url = 'https://www.tianyancha.com/search/?key='+keyword+"&checkFrom=searchBox"

    print(url)
    # result = urlopen(url).read();
    # print(result)
    #获得搜索结果页面   http://blog.csdn.net/qq_33348497/article/details/77851623
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

    driver = webdriver.PhantomJS(executable_path='/Users/penghaoyou/Documents/phantomjs-2.1.1-macosx/bin/phantomjs', desired_capabilities=dcap)
    driver.maximize_window()
    # driver.get(url)
    # driver.add_cookie({'jsid':'SEM-BAIDU-CG-SY-001063', 'TYCID':'284aafe0058611e8872dc55eb98f1c37', 'undefined':'284aafe0058611e8872dc55eb98f1c37', 'ssuid':'8167267020', 'RTYCID':'64567ae8475142c8a761e9091014521a','aliyungf_tc':'AQAAAI0efBziHQEAAkL+Z/B8RiRkCKHn','csrfToken':'CbneRPlIiDoz7XYdWdvYtJrR', 'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1517293441,1519782410,1519794489','token':'95f17d1a9dd14a6aa5715d2e0fbc3735','_utm':'7f8706ab0f6b42b9b7038e9cbe5506a1','tyc-user-info':'%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUwMDMyNjUxMCIsImlhdCI6MTUxOTgxOTEwNSwiZXhwIjoxNTM1MzcxMTA1fQ.V9SPBzAcSvoXXylQnpC2_ILPg3QnzEosAuFQ5y7fRBNI7FumP8XtmqtymjBZCZP61R9wtSLSV5SVkJfNysmTPg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218500326510%2522%257D','auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUwMDMyNjUxMCIsImlhdCI6MTUxOTgxOTEwNSwiZXhwIjoxNTM1MzcxMTA1fQ.V9SPBzAcSvoXXylQnpC2_ILPg3QnzEosAuFQ5y7fRBNI7FumP8XtmqtymjBZCZP61R9wtSLSV5SVkJfNysmTPg','_csrf':'D1ZoOOHdkCnz2Ce4joObSQ==','OA':'t3Xr7Fv6JQk0nRgXxQ1Pemt0csom9rH+q4ng/p1XnvreT8FOlE3Bhr7fnxm8Q4/QdULp57K8SRmoqzOfA2x6/lqoCPb1KZRUKBBga9ZoVGoJPASR3SuzBHYwh6Gh0ZqHqFTPHPHbe/3E5svBC7ulv7WEkA2R9Xxc4Nw6CLrtHrU=',' _csrf_bk':'c48e14ac7b6b0169cd6ad0295b69a1a1','Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1519819107'})

    driver.get(url)
    time.sleep(2)
    print(driver.page_source)
    driver.save_screenshot('2.png')  # 截图保存
    #从搜索结果中点击第一个结果
    driver.find_element_by_class_name('query_name').click()
    time.sleep(2)
    #抓取第一个结果的网页，匹配出需要的字段
    soup = BeautifulSoup(driver.page_source,"html.parser")
    basic_info_list = soup.find_all('p',class_="ng-binding ng-scope")
    data = []
    qiyemingcheng = driver.title.split('】')[1].split('信息查询')[0]
    data.append(qiyemingcheng)
    for i in basic_info_list:
        data.append(i.get_text().strip())
    return data

print(get_enterprise_data('科润智能'))