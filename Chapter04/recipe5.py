#문장에서 모든 다섯 글자 단어를 찾고 약어 만들기

import re

street = '21 Ramkrishna Road'
print(re.sub('Road', 'Rd', street)) #객체 street에 있는 것을 road를 rd로 약어 바꾸기

text = 'Diwali is a festival of light, Holi is a festival of color!'
print(re.findall(r"\b\w{5}\b", text))