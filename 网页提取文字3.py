# import urllib.request
#
#
# def getHtml(url):
#     html = urllib.request.urlopen(url).read()
#     return html
#
#
# def saveHtml(file_name, file_content):
#     # 注意windows文件命名的禁用符，比如 /
#     with open(file_name.replace('/', '_') + ".html", "wb") as f:
#         # 写文件用bytes而不是str，所以要转码
#         f.write(file_content)
#
#
# aurl = "http://search.chinalaw.gov.cn/law/searchTitleDetail?LawID=370030&Query=巡警&IsExact="
# html = getHtml(aurl)
# saveHtml("sduview", html)
#
# print("下载成功")
import sys
import requests
import importlib


def url_to_html(url):
    importlib.reload(sys)
    # sys.setdefaultencoding('utf-8')

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    html = requests.get(url, headers=header)
    html.encoding = html.apparent_encoding  # 从网页的内容中分析网页编码的方式
    fh = open('test.html', 'w', encoding='UTF-8')
    # fh.write(html.text.encode('iso-8859-1').decode('UTF-8'))  # 以iso-8859-1编码,以UTF-8解码
    fh.write(html.text)
    fh.close()
    # return html.text


url = 'http://cnzhuitao.cn/Ajitongjiling/'
# print(urltotext(url))
