def get_content(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
        return content


def get_TF(words, topK=10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    return sorted(tf_dic.items(), key=lambda x: x[1], reverse=True)[:topK]


def stop_words(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return [l.strip() for l in f]


stop_words('stop_words.utf8')


# 分词
def main():
    import jieba
    files = (get_content('10.txt'))

    split_words = [x for x in jieba.cut(files) if x not in stop_words('stop_words.utf8')]
    print('样本：' + files)
    print('\n样本分词效果：' + '/'.join(split_words))
    print('\n样本的topK（10）词：' + str(get_TF(split_words)))


main()