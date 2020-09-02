# coding=gbk
import jieba

sent = '为加强治安管理，维护社会秩序和公共安全，保护公民的合法权益，保障社会主义现代化建设的顺利进行，制定本条例。'
seq_list = jieba.cut(sent, cut_all=False)  # 精确模式
print('精确模式：', '/'.join(seq_list))
# seq_list = jieba.cut(sent, cut_all=True)
# print('全模式：', '/'.join(seq_list))

# seq_list = jieba.cut_for_search(sent)
# print('搜索引擎模式：', '/'.join(seq_list))
#
# seq_list = jieba.lcut_for_search(sent)
# print('返回列表：{}'.format(seq_list))