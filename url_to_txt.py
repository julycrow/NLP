# 通过html的方式
def url_to_html(url):
    import sys
    import requests
    import importlib

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


def html_to_txt(file, selector):
    import requests
    import bs4

    exampleFile = open(file, encoding='UTF-8')
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
    # elems = exampleSoup.select("#water_div")  # 返回一个带有id = "#water_div" 的元素，将这个Tag对象的列表保存在变量elems中
    # selector = '#best-content-2954257891 > p'
    elems = exampleSoup.select(selector)  # 返回一个带有id = selector 的元素，将这个Tag对象的列表保存在变量elems中
    # 元素的文本
    # print(elems[0].getText())
    return elems[0].getText()



if __name__ == '__main__':
    url = 'http://cnzhuitao.cn/Ajitongjiling/'
    url_to_html(url)  # 网页转html
    file = 'test.html'
    selector = 'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div:nth-child(1)'
    text = html_to_txt(file, selector)  # html提取文字
    # print(urltotext(url))
