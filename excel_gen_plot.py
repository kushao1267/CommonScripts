#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-18 14:42:44
# @Author  : Liu Jian (461698053@qq.com)
import xlsxwriter

global DATA, TITLE
TITLE = ['title1', 'title2', 'title3', 'title4', 'title5']
DATA = [
    ['1', '2', '3', '4', '5'],
    ['4', '5', '6', '7', '8'],
    ['9', '10', '11', '12', '13'],
    ['14', '15', '16', '17', '18']
]

# Insert an image.
# worksheet.insert_image('B5',  'logo.png')
# Insert row by row.


def excel_generator(name, titles, data):
    """
    功能：
            使用xlsxwriter生成excel文档, 储存在当前路径。
    参数：
            name = 'foo',  生成'foo.xlsx',  str
            titles = ['name1', 'name2', ...],  各列的标题, list
            data = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]],  1, 2, 3为一行.数据,  matrix
    """
    workbook = xlsxwriter.Workbook("{}.xlsx".format(name))
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    for title_n in range(len(titles)):
        worksheet.write(0, title_n, titles[title_n], bold)
    for row_num in range(len(data)):
        column_num = 0
        for elem in data[row_num]:
            worksheet.write(row_num + 1, column_num, elem)
            column_num += 1
    workbook.close()


def excel_ploter(name):
    """
    功能：
            使用xlsxwriter将excel文档生成图图表
    参数：
            name = 'foo',  生成'foo.xlsx',  str
            title = ['name1', 'name2', ...],  各列的标题, list
            data = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]],  1, 2, 3为一行.数据,  matrix
    """
    workbook = xlsxwriter.Workbook('chart.xlsx')
    worksheet = workbook.add_worksheet()

    # Create a new Chart object.
    chart = workbook.add_chart({'type': 'column'})

    # Write some data to add to plot on the chart.
    data = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
    ]

    worksheet.write_column('A1', data[0])
    worksheet.write_column('B1', data[1])
    worksheet.write_column('C1', data[2])

    # Configure the chart. In simplest case we add one or more data series.
    chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
    chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
    chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

    # Insert the chart into the worksheet.
    worksheet.insert_chart('A7', chart)

    workbook.close()


if __name__ == '__main__':
    excel_generator('foo', TITLE, DATA)
    excel_ploter('foo1')
