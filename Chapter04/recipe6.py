#자체 정규식 토크나이저 작성법

import re

raw = "I am big! It's the pictures that got small -3."
print(re.split(r' +', raw))

print(re.split(r'\W+', raw)) # ' '문자로만 구분 하기  \W는 문자와 숫자가 아닌 모든 문자 즉 
# 알파벳(a-z, A-Z)과 숫자(0-9)를 제외한 모든 문자를 의미합니다. +는 하나 이상의 연속된 문자


#re.findall() 함수를 이용해 문자열 raw에서 특정 패턴에 맞는 부분 문자열을 찾아 리스트로 반환
print(re.findall(r'\w+|\S\w*', raw)) 

#\w 는 모든 문자 w참고로 소문자
#\S는 공백이 아닌 문자를 의미합니다.
#\w*는 0개 이상의 알파벳이나 숫자
#GPT와 -3 등)를 찾는 데 유용합니다.