"""
中英互译脚本
"""
import click
from googletrans import Translator
import re


@click.command()
@click.option('--words', help='words to translate, only support chinese and english.')
@click.option('--file', help='file to translate.')
def translate(words, file):
    translator = Translator()
    # 读取文件
    if file:
        with open(file, 'r') as f:
            words_list = f.readlines()
        words = ''.join(words_list)

    print('\n' * 2)
    if not check_contain_chinese(words):
        # 翻译英文
        print('翻译英文结果如下:')
        t = translator.translate(words, dest='zh-CN').text
    else:
        # 翻译中文
        print('翻译中文结果如下:')
        t = translator.translate(words).text

    print('----------' * 8)
    print(t)
    print('----------' * 8)


def check_contain_chinese(check_str):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(check_str)
    if match:
        return True
    return False


if __name__ == '__main__':
    translate()
