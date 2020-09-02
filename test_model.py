def f1(path):
    with open(path, encoding='utf-8', errors='ignore') as f:

        all_tag = 0  # 记录所有的标记数
        loc_tag = 0  # 记录真实的地理位置标记数
        pred_loc_tag = 0  # 记录预测的地理位置标记数
        correct_tag = 0  # 记录正确的标记数
        correct_loc_tag = 0  # 记录正确的地理位置标记数

        states = ['B', 'M', 'E', 'S']
        for line in f:
            line = line.strip()
            if line == '': continue
            _, r, p = line.split()

            all_tag += 1

            if r == p:
                correct_tag += 1
                if r in states:
                    correct_loc_tag += 1
            if r in states: loc_tag += 1
            if p in states: pred_loc_tag += 1

        loc_P = 1.0 * correct_loc_tag / pred_loc_tag
        loc_R = 1.0 * correct_loc_tag / loc_tag
        print('精确率loc_P:{0}, 召回率loc_R:{1}, loc_F1:{2}'.format(loc_P, loc_R, (2 * loc_P * loc_R) / (loc_P + loc_R)))


f1('./crf/test.rst')
