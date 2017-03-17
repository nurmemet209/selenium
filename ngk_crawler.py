import xlwt
from selenium import webdriver
import time
import re

from selenium.webdriver.support.wait import WebDriverWait


class ExcelWriteHelper:
    '''
    Excel写操作
    '''
    file_name = ""

    def __init__(self, file_name, title_list, wb=None):
        self.file_name = file_name
        self.title_list = title_list
        if wb is not None:
            self.workbook = wb
            # 创建 sheet
            self.sheet = self.workbook.get_sheet(0)
        else:
            self.workbook = xlwt.Workbook()
            self.sheet = self.workbook.add_sheet("sheet 1")

        self.set_title()

    # 设置title（带样式）
    def set_title(self):
        title_style = xlwt.easyxf('font: bold 1')
        for i in range(len(self.title_list)):
            self.sheet.col(i).width = 1000 * (len(self.title_list[i]) + 1)
            self.sheet.write(0, i, self.title_list[i], title_style)

    def save(self):
        self.workbook.save(self.file_name)

    # 写整行数据
    def write_raw(self, raw_index, raw_data):
        for i in range(len(raw_data)):
            self.sheet.write(raw_index, i, str(raw_data[i]))

    # 填写指定单元格
    def write_cell(self, row, col, value):
        self.sheet.write(row, col, str(value))


# 写文件
# writer = ExcelWriteHelper("ngk.xls", ['品牌','车种车型', '排气量','上市年份', '发动机型式', 'NGK 火花塞', '库存编号', '推荐铱合金IX火花塞', '库存编号', '安装支数'])
#
#
#
# driver = webdriver.Chrome()
# driver.get("http://www.ngkntk.com.cn/customer/application")
# agree=driver.find_element_by_xpath('//*[@id="popup_ok"]')
# agree.click()
#
# ul=driver.find_element_by_xpath('//*[@id="export"]/ul')
# alist=driver.find_elements_by_xpath('//*[@id="export"]/ul/li/div[2]/a')
# row=1
# for brand in alist:
#
#     brand.location_once_scrolled_into_view
#     brand.click()
#     time.sleep(1)
#     brand_name=brand.text
#
#     table=driver.find_element_by_xpath('//*[@id="export"]/div[2]/table')
#     tr_list=table.find_elements_by_xpath("tbody/tr")
#     del tr_list[0]
#     for tr in tr_list:
#         tr.location_once_scrolled_into_view
#         td_list=tr.find_elements_by_xpath("td")
#         td_value_list=[]
#         td_value_list.append(brand_name)
#         for td in td_list:
#             td_value=td.text
#             td_value_list.append(td_value)
#         writer.write_raw(row, td_value_list)
#         row = row + 1
#
#
#
#
#
#
#
# writer.save()




import xlrd
import xlwt
from xlutils.copy import copy


class ExcelReadHelper:
    # 文件名称
    file_name = ""
    # 当前行
    current_raw = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.wb = xlrd.open_workbook(file_name)
        # 第一个sheet
        self.sh = self.wb.sheet_by_index(0)
        # 总行数
        self.all_raw = self.sh.nrows
        # 总列数
        self.all_col = self.sh.ncols

    def copy(self):
        return copy(self.wb)

    # 获取下一行
    def get_next_raw(self):
        self.current_raw = self.current_raw + 1
        if self.current_raw < self.all_raw:
            # 读取行数据
            raw_data = self.sh.row_values(self.current_raw)
            return raw_data

    # 返回指定的单元格值
    def get_cell(self, row, col):
        return self.sh.cell(row, col).value

    # 返回指定的列数据
    def get_col(self, col):
        return self.sh.col_values(col)

    # 返回指定的列指定行范围的数据
    def get_col_by_range(self, col, row_s, row_e):
        return self.sh.col_values(col, row_s, row_e)

    # 返回指定的行数据
    def get_row(self, row):
        return self.sh.row_values(row)

    # 返回指定的行的指定列范围的数据
    def get_row_by_range(self, row, col_s, col_e):
        return self.sh.row_values(row, col_s, col_e)


class ExcelWriteHelper:
    '''
    Excel写操作
    '''
    file_name = ""

    def __init__(self, file_name, title_list, wb=None):
        self.file_name = file_name
        self.title_list = title_list
        if wb is not None:
            self.workbook = wb
            # 创建 sheet
            self.sheet = self.workbook.get_sheet(0)

        else:
            self.workbook = xlwt.Workbook()
            self.sheet = self.workbook.add_sheet("sheet 1")
            self.set_title()

    # 设置title（带样式）
    def set_title(self):
        title_style = xlwt.easyxf('font: bold 1')
        for i in range(len(self.title_list)):
            self.sheet.col(i).width = 1000 * (len(self.title_list[i]) + 1)
            self.sheet.write(0, i, self.title_list[i], title_style)

    def save(self):
        self.workbook.save(self.file_name)

    # 写整行数据
    def write_raw(self, raw_index, raw_data):
        for i in range(len(raw_data)):
            self.sheet.write(raw_index, i, str(raw_data[i]))

    # 填写指定单元格
    def write_cell(self, row, col, value):
        self.sheet.write(row, col, str(value))


# 写文件
# writer = ExcelWriteHelper("mytest.xls", ['姓名', '学号', '数学成绩'])
# writer.save()

reader = ExcelReadHelper("ngk.xls")
writer = ExcelWriteHelper("test.xlsx", ['火花塞', '车型'])
type_list = reader.get_col(5)
row = 1
for m in range(len(type_list)):
    name = type_list[m]
    data_list = []
    p_list = []
    for n in range(len(type_list)):
        name_ = type_list[n]

        if name == name_:
            p_list.append(reader.get_cell(n, 1))
    data_list.append(name)
    data_list.append(" ".join(p_list))
    writer.write_raw(row, data_list)
    row = row + 1

writer.save()
