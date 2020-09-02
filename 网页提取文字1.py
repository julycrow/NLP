# 需选定网页中的位置
from requests_html import HTMLSession
import pandas as pd


def get_text_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            # mylink = list(result.absolute_links)[0]  # result.absolute_links 为一个集合，list转换为列表
            mylist.append(mytext)
        return mylist
    except:
        return None


session = HTMLSession()  # 建立一个会话（session），即让Python作为一个客户端，和远端服务器交谈。
url = 'http://search.chinalaw.gov.cn/law/searchTitleDetail?LawID=370030&Query=巡警&IsExact='
r = session.get(url)  # session 的 get 功能，把这个链接对应的网页取回来
# print(r.html.absolute_links)  # 打印出超链
sel = '#water_div > p'  #
results = r.html.find(sel)  # 查找 sel 对应的位置，把结果存到 results 变量中
# print(get_text_from_sel(sel))

df = pd.DataFrame(get_text_from_sel(sel))
df.columns = ['characters']
print(df)
