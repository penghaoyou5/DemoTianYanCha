# -*- coding: utf-8 -*-
"""
主函数进行表格的输入输出的
"""

import file_csdn3_text_parse
import file_csdn3_xslx_parse
import file_csdn3_request
import time
import xlsxwriter

# 创建新表格
global worksheet
workbook = xlsxwriter.Workbook("result"+ time.time() +".xls")
worksheet = workbook.add_worksheet()


#获取公司名称
company_dict = file_csdn3_xslx_parse.read_file(1,3)
for line_num in company_dict.keys():
    company_name = company_dict[line_num]
    #原始网络请求获取文本信息
    file_csdn3_request.main(company_name)
    try:
        #文本信息解析
        company_obj = file_csdn3_text_parse.main()
        #写入文件中
        print line_num,company_name
        file_csdn3_xslx_parse.write_file(worksheet,line_num,company_obj)
    except Exception as e:
        print e
    time.sleep(60)



workbook.close()