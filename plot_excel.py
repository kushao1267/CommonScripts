#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-18 14:42:44
# @Author  : Liu Jian (461698053@qq.com)
import xlsxwriter

global DATA, TITLE
TITLE = ['name1', 'name2', 'name3', 'name4', 'name5']
DATA = [
    ['1', '2', '3', '4', '5'],
    ['4', '5', '6', '7', '8'],
    ['9', '10', '11', '12', '13'],
    ['14', '15', '16', '17', '18']
]

# Insert an image.
# worksheet.insert_image('B5', 'logo.png')
# Insert row by row.


def ExcelGenerator(name, title, data):
    """
        功能：
                使用xlsxwriter生成excel文档,储存在当前路径。
        参数：
                name = 'foo', 生成'foo.xlsx', str
                title = ['name1','name2',...], 各列的标题,list
                data = [[1,2,3,],[4,5,6],[7,8,9]], 1,2,3为一行.数据, matrix
    """
    workbook = xlsxwriter.Workbook("{}.xlsx".format(name))
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    for n in range(len(title)):
        worksheet.write(0, n, title[n], bold)
    for row_num in range(len(data)):
        column_num = 0
        for elem in data[row_num]:
            worksheet.write(row_num + 1, column_num, elem)
            column_num += 1
    # Write a total using a formula.
    worksheet.write(row_num + 2, 0, 'Total')
    worksheet.write(row_num + 2, 1, '=SUM(B1:B4)')
    workbook.close()


def Ploter(name):
    """
        功能：
                使用xlsxwriter将excel文档生成图图表
        参数：
                name = 'foo', 生成'foo.xlsx', str
                title = ['name1','name2',...], 各列的标题,list
                data = [[1,2,3,],[4,5,6],[7,8,9]], 1,2,3为一行.数据, matrix
    """
    intab = "0123456789"
    outtab = "ABCDEFGHIJ"
    trantab = str.maketrans(intab, outtab)

    workbook = xlsxwriter.Workbook("{}.xlsx".format(name))
    worksheet = workbook.add_worksheet()

    # Add the worksheet data to be plotted.
    for n in range(len(DATA)):
        worksheet.write_column('{}1'.format(
            str(n).translate(trantab)), DATA[n])

    # Type of chart
    chart = workbook.add_chart({'type': 'line'})

    # Add a series to the chart.
    chart.add_series({'values': '=Sheet1!$A$1:$A${}'.format(len(DATA[0]))})

    # Insert the chart into the worksheet.
    worksheet.insert_chart('G1', chart)

    workbook.close()


if __name__ == '__main__':
    ExcelGenerator('foo', TITLE, DATA)
    Ploter('foo1')
