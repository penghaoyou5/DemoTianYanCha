# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys

"""
进行表格解析
"""

import xlsxwriter
import file_csdn3_text_parse

#行数 公司信息
def write_file(worksheet,line_number,company_obj):
    print line_number


    worksheet.write(line_number, 1, company_obj.company_name)
    worksheet.write(line_number, 2, company_obj.Legal_representative)
    worksheet.write(line_number, 3, company_obj.regist_mony)
    worksheet.write(line_number, 4, company_obj.regist_time)
    worksheet.write(line_number, 5, company_obj.regist_address)
    worksheet.write(line_number, 6, company_obj.phone)





import xlrd
def read_file(line_num_start,line_num_end):
    company_dict = {}
    workbook = xlrd.open_workbook('source.xls')
    booksheet = workbook.sheets()[0]
    for lin_num in range(line_num_start,line_num_end):
        company_name = booksheet.cell_value(lin_num, 0)
        company_dict[lin_num] = company_name
    return company_dict


def write_source_file():
    # 创建新表格
    global worksheet
    workbook = xlsxwriter.Workbook("source.xls")
    worksheet = workbook.add_worksheet()
    worksheet.write(1,0,"北京呼家楼宾馆有限公司")
    worksheet.write(2, 0, "国盈控股有限公司")
    worksheet.write(3, 0, "北京汽车摩托车联合制造公司")
    worksheet.write(4, 0, "北京呼家楼基金管理有限公司")
    worksheet.write(5, 0, "展盈投资控股有限公司")
    worksheet.write(6, 0, "泛亚大陆（北京）煤层气资源投资有限公司")
    worksheet.write(7, 0, "悦读名品文化传媒（北京）有限公司")
    worksheet.write(8, 0, "北京泰岳恒通文化顾问有限公司")
    worksheet.write(9, 0, "中安佳业（北京）投资有限公司")
    worksheet.write(10, 0, "黑桃（北京）投资咨询有限公司")
    worksheet.write(11, 0, "北京中佳华天投资顾问有限公司")
    worksheet.write(12, 0, "普康林生物技术（北京）有限公司")


    workbook.close()




if __name__ == '__main__':
    # company_obj = file_csdn3_text_parse.main()
    # write_file(3,company_obj)

    # company_dict = read_file(3,7)
    # for k in company_dict.keys():
    #     print k,company_dict[k]


    write_source_file()
