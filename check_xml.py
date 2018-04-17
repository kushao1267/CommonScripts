# coding=utf-8
"""
Authority:
    tangmengyue@raisecom.com
Date:
    2018-3-30 00:10
Update:
    2018-4-4 17:18
Usage:
    将该脚本与要检测的目录放于同一级，并且XML_ROOT_DIRECTORY改为该目录名
"""

import os
from xml.dom import expatbuilder


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
        file_content = _ignore_xml_comment(file)
        builder = expatbuilder.ExpatBuilderNS()
        try:
            builder.parseString(file_content)
        except Exception as e:
            if "multi-byte" not in str(e):
                print("[path]:{0}\t[error]:{1}\r\n".format(file, e))


def _ignore_xml_comment(file):
    """
        忽略xml的注释
    """
    no_comment_file = ""
    with open(file, "r") as f:
        line = f.readline()
        while line:
            if "<!--" in line:
                if "-->" in line:
                    # 忽略该行
                    line = f.readline()
                    continue
                next_line = f.readline()
                while next_line and "-->" not in next_line:
                    next_line = f.readline()
                # 非注释行
                line = f.readline()
            no_comment_file += line
            line = f.readline()
    return no_comment_file


if __name__ == "__main__":
    print("Check begin:")
    print("------" * 10 + "\r\n")
    for dire in XML_ROOT_DIRECTORY_LIST:
        xml_files = acquire_xml_files(CURRENT_DIRECTORY + "/" + dire)
        parse_xml_files(xml_files)
    print("------" * 10 + "\r\n")
    print("Completed!")
