# -*- coding: utf-8 -*-
import requests
import re
import os


def get_link(html_chapter_str):
    '''

    :param html_chapter_str: html字符串
    :return: 小说章节的链接列表
    '''
    print('获取链接')
    link_list = []
    block = re.findall('<h2>(.*?)<!-- =footer= -->', html_chapter_str, re.S)[0]
    url_list = re.findall('<li><a href="(.*?)"', block, re.S)
    for url in url_list:
        link_list.append('http://www.wuyanxia.net' + url)
    return link_list


def get_chaptername_and_content(url):
    '''

    :param link_list: 链接列表
    :return: 返回章节名和正文内容列表
    '''
    print('获取章节与内容')
    html = requests.get(url)
    html_str = html.content.decode('GBK')
    block = re.findall('<!--主内容-->(.*?)</div>', html_str, re.S)[0]
    chaptename = re.findall(
        '<span id="htmltimu">(.*?)</span>',
        html_str,
        re.S)[0]
    chaptename = chaptename.replace(' ', '')
    content = re.findall('</table>(.*)', block, re.S)[0]
    # print(content)
    content = content.replace('&nbsp;', ' ')
    content = content.replace('<br />', '')
    return [chaptename, content]


def save_file(chaptername, content):
    print('存储文件')
    print(chaptername)
    file_path = os.path.join('刀剑神域小说', chaptername + '.txt')
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(content)


if __name__ == '__main__':
    html_chapter = requests.get('http://www.wuyanxia.net/read/77374.html')
    html_chapter_str = html_chapter.content.decode('GBK')
    link_list = get_link(html_chapter_str)
    os.makedirs('刀剑神域小说', exist_ok=True)
    for url in link_list:
        try:
            list = get_chaptername_and_content(url)
            save_file(list[0], list[1])
        except Exception as e:

            pass
        finally:
            pass
