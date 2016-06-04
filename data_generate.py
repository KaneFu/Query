#!/usr/bin/env python
# coding=utf-8

import numpy as np
import codecs


all_text = u"国家知识啊沙发你就从年少你擦拭的女潍坊无其他为其他逼我去不求vbuqevuqehvusddb请问去无人区无法是是产权局知识产权发展研究中心北京自然博物馆地衣系统分类学山西医科大学政府科技项目的立项申报你撒谎发沙发is发is发is分请问你去你去我发你赛场按时发才到家挨罚艾萨司法局盎司附近吃啊我按实际覅按时发教案差发发阿萨是发顺丰"
all_char = [cha for cha in all_text]
length = len(all_char)

new_words = []

for ii in range(30000):
	char_index = np.random.randint(1,length,(1,np.random.randint(1,16)))[0]
	res = [all_char[index] for index in char_index]
	word = ''.join(res)
	new_words.append(word)

file_name = 'more_data.txt'
with codecs.open(file_name,"w","utf-8") as f:
	f.write('\n'.join(new_words))
	f.close()

