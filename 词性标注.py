import jieba.posseg as psg

sent = '扰乱车站、码头、民用航空站、市场、商场、公园、影剧院、娱乐场、运动场、展览馆或者其他公共场所的秩序的'
seg_list = psg.cut(sent)
print(' '.join(['{0}/{1}'.format(w, t) for w, t in seg_list]))
