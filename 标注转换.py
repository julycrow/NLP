# coding=utf8


def tag_line(words, mark):  # 每行的标注转换
    chars = []
    tags = []
    temp_word = ''  # 用于合并组合词，如[中央/n 电视台/n]n
    for word in words:
        word = word.strip('\t ')  # 删除字符串头尾的\t
        if temp_word == '':
            bracket_pos = word.find('[') # 找到返回下标，否则返回-1
            w, h = word.split('/')
            if bracket_pos == -1:
                if len(w) == 0: continue  # 跳出本次循环，执行下一次
                chars.extend(w)
                if h == 'ns':
                    tags += ['S'] if len(w) == 1 else ['B'] + ['M'] * (len(w) - 2) + ['E']  # 长度为1 标记 s；长度>1 标记 B M……M E
                else:
                    tags += ['O'] * len(w)
            else:
                w = w[bracket_pos + 1:]
                temp_word += w
        else:
            bracket_pos = word.find(']')
            w, h = word.split('/')
            if bracket_pos == -1:
                temp_word += w
            else:
                w = temp_word + w
                h = word[bracket_pos + 1:]  # 整个[……]的词性
                temp_word = ''
                if len(w) == 0: continue
                chars.extend(w)
                if h == 'ns':
                    tags += ['S'] if len(w) == 1 else ['B'] + ['M'] * (len(w) - 2) + ['E']
                else:
                    tags += ['O'] * len(w)

    assert temp_word == ''
    return (chars, tags)


def corpusHandler(corpusPath): # 加载数据，调用tag_line，保存转换结果，corpusPath为文件
    import os
    root = os.path.dirname(corpusPath)  # 返回文件路径
    with open(corpusPath, 'r', encoding='utf-8', errors='ignore') as corpus_f, \
            open(os.path.join(root, 'train.txt'), 'w') as train_f, \
            open(os.path.join(root, 'test.txt'), 'w') as test_f:  # 把路径和文件名合成一个路径，即root\train.txt

        pos = 0
        for line in corpus_f:
            line = line.strip('\r\n\t ')  # 删除头尾的\r和\r和\t
            if line == '': continue
            isTest = True if pos % 5 == 0 else False  # 抽样20%作为测试集使用
            words = line.split()[1:]  # 以空格为分隔符，包含\n，分成的个数无限制，第一个不要是因为文件里每行第一个是日期（没用）
            if len(words) == 0: continue
            line_chars, line_tags = tag_line(words, pos)
            saveObj = test_f if isTest else train_f  # saveObj类似一个中间的桶，每5个中第一个倒在测试集，后四个倒在训练集
            for k, v in enumerate(line_chars):  # enumerate将line_chars转换成索引序列，如[(0, 'Spring'), (1, 'Summer')···]
                saveObj.write(v + '\t' + line_tags[k] + '\n')  # 词\t词性
            saveObj.write('\n')
            pos += 1


if __name__ == '__main__':
    corpusHandler('./crf/people-daily.txt')
