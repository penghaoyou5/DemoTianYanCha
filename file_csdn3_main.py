#!/System/Library/Frameworks/Python.framework/Versions/2.7
# -*- coding: utf-8 -*-
"""
主函数进行表格的输入输出的
"""

import file_csdn3_text_parse
import file_csdn3_xslx_parse
import file_csdn3_request
import time
import xlsxwriter
import os
import file_csdn3_util

#新的表格名字
table_name = "result"+ str(time.time()) +".xls";

# 创建新表格
workbook = xlsxwriter.Workbook(table_name)
worksheet = workbook.add_worksheet()
workbook.close()

#获取公司名称
company_dict = file_csdn3_xslx_parse.read_file(1,10)
for line_num in company_dict.keys():
    company_name = company_dict[line_num]
    #原始网络请求获取文本信息
    file_csdn3_request.main_while(company_name)

    print line_num, company_name
    try:
        #文本信息解析
        company_obj = file_csdn3_text_parse.main()
        #写入文件中
        file_csdn3_xslx_parse.write_file_exist(table_name,line_num,company_obj)
    except Exception as e:
        file_csdn3_util.write_error(e)
        print e
    time.sleep(60)



