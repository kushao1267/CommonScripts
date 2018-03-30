# coding=utf-8
"""
Authority:
    tangmengyue@raisecom.com
Date:
    2018-3-30 00:10
Usage:
    将该脚本与要检测的目录放于同一级，并且XML_ROOT_DIRECTORY改为该目录名
"""

import os
from xml.dom import minidom

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))  # 当前文件的路径
XML_ROOT_DIRECTORY_LIST = ["epon", "server", "client"]  # xml文件所在的根目录名称,可配置


def acquire_xml_files(path):
    """
        获取目录下所有的xml文件
    """
    xml_files = []
    for dirpath, _, filenames in os.walk(path):
        for name in filenames:
            _file = os.path.join(dirpath, name)
            if _file.endswith(".xml"):
                xml_files.append(_file)
    return xml_files


def parse_xml_files(xml_files):
    """
        解析所有的xml文件,返回错误日志
    """
    for file in xml_files:
        try:
            minidom.parse(file)
        except Exception as e:
            print("[path]:{0}\t[error]:{1}\n".format(file, e))


if __name__ == "__main__":
    print("开始检测:")
    print("------" * 10 + "\n")
    for dire in XML_ROOT_DIRECTORY_LIST:
        xml_files = acquire_xml_files(CURRENT_DIRECTORY + "/" + dire)
        parse_xml_files(xml_files)
    print("------" * 10 + "\n")
    print("检测完成!")
