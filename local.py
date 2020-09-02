def load_model(path):
    import os, CRFPP
    if os.path.exists(path):
        return CRFPP.Tagger('-m {0} -v 3 -n2'.format(path))  # 模型加载
    return None


def locationNER(text):
    tagger = load_model('./crf/model')

    for c in text:
        tagger.add(c)

    result = []
    tagger.parse()
    word = ''
    for i in range(0, tagger.size()):
        for j in range(0, tagger.xsize()):
            ch = tagger.x(i, j)
            tag = tagger.y2(i)
            if tag == 'B':
                word = ch
            elif tag == 'M':
                word += ch
            elif tag == 'E':
                word += ch
                result.append(word)
            elif tag == 'S':
                word = ch
                result.append(word)

    return result


from url_to_txt import url_to_html
from url_to_txt import html_to_txt
import re

if __name__ == '__main__':
    text = '我爱合肥'
    print(text, locationNER(text), sep='==> ')


    text = '乌鲁木齐、克拉玛依19县级市——石河子、阿拉尔市、图木舒克、五家渠、哈密、吐鲁番、阿克苏、喀什、和田、伊宁、塔城、阿勒泰、奎屯、博乐、昌吉、阜康、库尔勒、阿图什、乌苏2，【西藏】：1地级市 - 拉萨县级市 - ' \
           '日喀则3，【宁夏】：5地级市——银川、石嘴山、吴忠、固原、中卫 '
    print(text, locationNER(text), sep='==> ')

    url = 'https://baike.baidu.com/item/合肥/210419?fr=aladdin'
    url_to_html(url)  # 网页转html
    file = 'test.html'
    selector = 'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div'
    text = html_to_txt(file, selector)  # html提取文字
    print(text, locationNER(text), sep='==> ')

    url = 'https://baike.baidu.com/item/合肥/210419?fr=aladdin'
    url_to_html(url)  # 网页转html
    file = 'test.html'
    selector = 'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div:nth-child(54)'
    text = html_to_txt(file, selector)  # html提取文字
    print(text, locationNER(text), sep='==> ')
