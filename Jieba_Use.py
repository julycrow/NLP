# coding=gbk
import jieba

sent = 'Ϊ��ǿ�ΰ�����ά���������͹�����ȫ����������ĺϷ�Ȩ�棬������������ִ��������˳�����У��ƶ���������'
seq_list = jieba.cut(sent, cut_all=False)  # ��ȷģʽ
print('��ȷģʽ��', '/'.join(seq_list))
# seq_list = jieba.cut(sent, cut_all=True)
# print('ȫģʽ��', '/'.join(seq_list))

# seq_list = jieba.cut_for_search(sent)
# print('��������ģʽ��', '/'.join(seq_list))
#
# seq_list = jieba.lcut_for_search(sent)
# print('�����б�{}'.format(seq_list))