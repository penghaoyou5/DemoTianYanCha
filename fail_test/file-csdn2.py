# -*- coding: utf-8 -*-
import time
import sys
import urllib
import requests


def main():
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2',
               'Connection': 'keep-alive',
               'DNT': '1',
               'Host': 'www.tianyancha.com',
               'Referer': 'http://www.tianyancha.com/search?key=%E7%99%BE%E5%BA%A6&checkFrom=searchBox',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
               }

    cookies = {'aliyungf_tc': 'AQAAAInSEClDxQUAftHidO+PzCmdPZot',
               'ssuid': '3986673831',
               'bannerStorageV2': '%22false%22',
               '_pk_ref.1.e431': '%5B%22%22%2C%22%22%2C1498801845%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Do5N6sHrB-gmAwl5M4IyAj3G-5IwlRrODDLv9KztH10ivG8HhNHkgDVgRGREFnnDo%26wd%3D%26eqid%3D857f04a80002baa6000000045955e633%22%5D',
               'token': '0be5e638129c4f31b919a967874008b9',
               '_utm': 'd6268574eb574651adf74cccc7544227',
               '_pk_id.1.e431': 'c993f4ee7aa80f31.1498532324.2.1498803205.1498801845.',
               'paaptp': 'ac2b22f83d9dd0dd86d47a0ed395ab25daf20e81e80534fe7315cf7a1f2fb',
               'csrfToken': 'mVLfAuO0VxQSUCvQ1Iip_cGu',
               'TYCID': '8b7b7d5061f411e7bd5589439b03dd9e',
               'uccid': '17cd6a2a4cf16ac20363e1b85bee6b90',
               'tyc-user-info': 'eyJuZXciOiIxIiwidG9rZW4iOiJleUpoYkdjaU9pSklVelV4TWlKOS5leUp6ZFdJaU9pSXhNekU0TkRNNU1EazROeUlzSW1saGRDSTZNVFE1T1RNd09EazRNaXdpWlhod0lqb3hOVEUwT0RZd09UZ3lmUS5TSENlRksweGdnd09UcEtDUnlpNXVpTFg4UVBwbXZJNmFOUi1ITjhCbVltNEZaT0hTeDhENDJJQ3E0T295c1ZFSVppRHEya2ZEZElmSGpsaFF5dV9ydyIsInN0YXRlIjoiMCIsInZudW0iOiIwIiwib251bSI6IjAiLCJtb2JpbGUiOiIxMzE4NDM5MDk4NyJ9',
               'bannerFlag': 'true',
               'Qs_lvt_117460': '1499308873%2C1499309809%2C1499390608',
               '_csrf': 'N/4TCyFkbN17DmLl2qSx+Q==',
               'OA': 'F6nGwYzI0K34U50NUXjCQ/RdisJkPVhyuvaz/ULhAdH9wGFBF+oY9SNo41xfg8ChEnKmkDW9KccidaKN4NUM7RY0fvt6ry12S005VjpHV9M=',
               '_csrf_bk': 'ababd67a90e3e88a85e813986cb58d6b',
               'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1498532730,1498801845,1499308866,1499309809',
               'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1499400842',
               'Qs_pv_117460': '1553841720118954500%2C1189009320365233400%2C4541963271723247600%2C1868246178729382000%2C1343361850682038000'
               }
    keyword = '百度'  # 要搜索的公司

    startUrl = 'http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % urllib.quote(keyword)

    resultPage = requests.get(startUrl, headers=headers, cookies=cookies)  # 在请求中设定头，cookie

    time.sleep(10)

    with open('tyc_demo.txt', 'w') as of:
        of.write(resultPage.text)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
