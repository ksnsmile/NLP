# 정규표현식-$와 ^,단어의 시작과 끝이 아닌 단어를 사용하는 방법

import re

def text_match(text, patterns):
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Pattern to test start and end with")
print(text_match("abbc", "^a.*c$")) # '.'은 줄바꿈을 제외한 모든 문자와 일치/ 

print("Begin with a word")
print(text_match("Tuffy eats pie, Loki eats peas!", "^\w+")) #'\W' 는 모든 영숫자(밑줄등)고 '+'은 이것이 하나 이상 출현

# 0번 이상의 공백이 아닌 문자(\S)가 나올 수 있으며, *?는 비탐욕적(최소 매칭)으로 매칭하라는 뜻입니다. 하나만 매칭한다는것 
#문자열이 어떻게 끝나는지만 확인하는 거여서 그럼  peas!만 본다.
print("End with a word and optional punctuation")
print(text_match("Tuffy eats pie, Loki eats peas!", "\w+\S*?$")) 


# \B는 "단어 경계가 아님"을 의미
# u는 문자 'u'
#\Bu\B는 단어의 시작이나 끝이 아닌 위치에 있는 'u'를 찾는 패턴
print("Finding a word which contains character, not start or end of the word")
print(text_match("Tuffy eats pie, Loki eats peas!", "\Bu\B"))