import bs4

exampleFile = open('example.html', encoding='UTF-8')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")  # 返回一个带有id = "water_div" 的元素，将这个Tag对象的列表保存在变量elems中
elems = exampleSoup.select("#water_div")
print(elems[0].getText())  # 列表中只有一个Tag对象，只有一次匹配。打印元素的文本
