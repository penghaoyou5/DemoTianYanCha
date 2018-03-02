# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
"""

<div class="b-c-white search_result_container">
         <div class="search_result_single search-2017 pb25 pt25 pl30 pr30 ">
          <div class="mr20 search_left_icon b-c-white position-rel">
           <img alt="北京百度网讯科技有限公司" onerror="this.src='https://static.tianyancha.com/wap/images/searchLogo918.png'" src="https://img.tianyancha.com/logo/lll/36089e162a250252363a05d74b96185b.png@!watermark01"/>
           <div class="claim_icon_ok position-abs" style="left:-20px;bottom: -10px;">
           </div>
          </div>
          <div class="search_right_item ml10">
           <div>
            <a class="query_name sv-search-company f18 in-block vertical-middle" href="https://www.tianyancha.com/company/22822" style="word-break: break-all;font-weight: 600;" target="_blank" tyc-event-ch="CompanySearch.Company" tyc-event-click="">
             <span>
              北京
              <em>
               百度
              </em>
              网讯科技有限公司
             </span>
            </a>
            <div class="statusTypeNor in-block f12 in-block vertical-middle ml10 statusType1">
             开业
            </div>
            <!--<div class="c-white claim_yel ml10" onclick="claimCompany(22822)">我要认证</div>-->
           </div>
           <div class="search_row_new pt20">
            <div>
             <div class="title overflow-width" style="padding-left: 0;">
              法定代表人：
              <a class="legalPersonName hover_underline" href="https://www.tianyancha.com/human/2020172991-c22822" target="_blank" title="梁志祥">
               梁志祥
              </a>
             </div>
             <div class="title overflow-width">
              注册资本：
              <span title="217128 万人民币">
               217128 万人民币
              </span>
             </div>
             <div class="title overflow-width" style="border-right: none">
              注册时间：
              <span title="2001-06-05 00:00:00.0">
               2001-06-05
              </span>
             </div>
             <div class="in-block vertical-middle float-right lh-1em">
              <span class="pr30 ">
               北京
              </span>
              <span class="c9 f20">
               97
              </span>
              <span class="f12 c9">
               分
              </span>
             </div>
            </div>
            <div>
             <div class="add pb5">
              <span class="sec-c3">
               联系电话：
              </span>
              <span class="overflow-width over-hide vertical-bottom in-block" style="max-width:500px;">
               010-59928888
              </span>
              <span>
               <script type="text/html">
                ["010-59928888","56798989","59928888"]
               </script>
               <span class="ml20 c9 hover_underline point" onclick="openPhonePopup(this)">
                查看更多
               </span>
              </span>
             </div>
            </div>
            <div>
             <div class="add">
              <span class="sec-c3">
               公司简称
              </span>
              <span>
               ：
              </span>
              <span class="overflow-width over-hide vertical-bottom in-block" style="max-width:500px;">
               <em>
                百度
               </em>
              </span>
             </div>
            </div>
           </div>
           <div class="pt15">
            <div class="searchItemType company-tag">
             <span>
              高新企业
             </span>
            </div>
           </div>
          </div>
         </div>
         <div class="search_result_single search-2017 pb25 pt25 pl30 pr30 ">
          <div class="mr20 search_left_icon b-c-white position-rel">
           <img alt="百度在线网络技术（北京）有限公司" onerror="this.src='https://static.tianyancha.com/wap/images/searchLogo918.png'" src="https://img.tianyancha.com/logo/lll/e2331a5fd8e089b10f504afa8c07c3fe.png@!watermark01"/>
           <div class="claim_icon_ok position-abs" style="left:-20px;bottom: -10px;">
           </div>
          </div>

"""


def main():
    company_obj = Company_message()
    soup = BeautifulSoup(open('tyc_demo2.txt'), "lxml")
    # print soup.prettify()
    print "======================================"
    import re

    first_link = soup.find("a", class_= re.compile("query_name sv-search-company f18 in-block vertical-middle"))
    # print (first_link)
    #
    # print '==========='
    #
    # for sibling in first_link.next_siblings:
    #     print((sibling))
    #
    # # print first_link.next_sibling
    #
    # print '==========='
    # name_link_parent = first_link.find_parent()
    #
    # for sibling in name_link_parent.next_siblings:
    #     print((sibling))

    # print soup.find('a',class_= "legalPersonName hover_underline")
    # print soup.next

    # print first_link.find_parent()

    # print BeautifulSoup(str(first_link.find_parent().find_parent()), "lxml").prettify()

    need_element = first_link.find_parent().find_parent()

    need_childs = need_element.children
    # print dir(need_childs)
    #北京百度网讯科技有限公司
    company_name = need_childs.next().children.next().get_text()
    print company_name
    company_obj.company_name = company_name;
    """
    <div><div class="title overflow-width" style="padding-left: 0;">法定代表人：<a class="legalPersonName hover_underline" href="https://www.tianyancha.com/human/2020172991-c22822" target="_blank" title="梁志祥">梁志祥</a></div><div class="title overflow-width">注册资本：<span title="217128 万人民币">217128 万人民币</span></div><div class="title overflow-width" style="border-right: none">注册时间：<span title="2001-06-05 00:00:00.0">2001-06-05</span></div><div class="in-block vertical-middle float-right lh-1em"><span class="pr30 ">北京</span><span class="c9 f20">97</span><span class="f12 c9">分</span></div></div>
    <div><div class="add pb5"><span class="sec-c3">联系电话：</span><span class="overflow-width over-hide vertical-bottom in-block" style="max-width:500px;">010-59928888</span><span><script type="text/html">["010-59928888","56798989","59928888"]</script><span class="ml20 c9 hover_underline point" onclick="openPhonePopup(this)">查看更多</span></span></div></div>
    <div><div class="add"><span class="sec-c3">公司简称</span><span>：</span><span class="overflow-width over-hide vertical-bottom in-block" style="max-width:500px;"><em>百度</em></span></div></div>
    
    """
    need_childs2 = need_childs.next().children

    """
    <div class="title overflow-width" style="padding-left: 0;">法定代表人：<a class="legalPersonName hover_underline" href="https://www.tianyancha.com/human/2020172991-c22822" target="_blank" title="梁志祥">梁志祥</a></div>
    <div class="title overflow-width">注册资本：<span title="217128 万人民币">217128 万人民币</span></div>
    <div class="title overflow-width" style="border-right: none">注册时间：<span title="2001-06-05 00:00:00.0">2001-06-05</span></div>
    <div class="in-block vertical-middle float-right lh-1em"><span class="pr30 ">北京</span><span class="c9 f20">97</span><span class="f12 c9">分</span></div>
    """
    need_childs3 = need_childs2.next().children
    #法人代表
    Legal_representative = need_childs3.next().get_text().split('：')[1]
    print Legal_representative
    company_obj.Legal_representative = Legal_representative
    #注册资本
    regist_mony = need_childs3.next().get_text().split('：')[1]
    print regist_mony
    company_obj.regist_mony = regist_mony

    #注册时间
    regist_time = need_childs3.next().get_text().split('：')[1]
    print regist_time
    company_obj.regist_time = regist_time


    #注册地址
    regist_address = need_childs3.next().children.next().get_text()
    print regist_address
    company_obj.regist_address = regist_address


    #联系电话p
    phone = need_childs2.next().get_text().split('：')[1].split('[')[0]
    print phone
    company_obj.phone = phone
    # for child in need_childs3:
    #     print child.get_text()
    # print need_childs3
        # print child
    # print need_element.get_text()
    return company_obj


class Company_message:
    company_name = "名字"
    Legal_representative ="法人"
    regist_mony = "金额"
    regist_time = "时间"
    regist_address = "地址"
    phone ="电话"

if __name__ == '__main__':
    main()
