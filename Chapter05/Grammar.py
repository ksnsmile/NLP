#자체 문법 작성 학습

import nltk
import string
from nltk.parse.generate import generate #generate: NLTK의 모듈 중 하나로, 정의된 규칙에 따라 문자열을 생성합니다.

productions = [
    "ROOT -> WORD",
    "WORD -> ' '",
    "WORD -> NUMBER LETTER", #숫자와 문자의 조합
    "WORD -> LETTER NUMBER", #문자와 숫자의 조합
]

digits = list(string.digits) #string.digits는 0부터 9까지 숫자 생성
for digit in digits[:4]:
    productions.append("NUMBER -> '{w}'".format(w=digit))

letters = "' | '".join(list(string.ascii_lowercase)[:4]) #string.ascii_lowercase[:4]는 알파벳 소문자 중 처음 네 개인 ['a', 'b', 'c', 'd']를 가져옵니다.
productions.append("LETTER -> '{w}'".format(w=letters))

grammarString = "\n".join(productions)


# =============================================================================
# nltk.CFG.fromstring(grammarString)을 사용하여 문법을 CFG 객체로 변환합니다. 
# 이 객체를 통해 생성 규칙을 따르는 문장을 생성하거나 분석할 수 있습니다.
# CFG 객체는 문법을 정의하는 규칙
# =============================================================================

grammar = nltk.CFG.fromstring(grammarString)

print(grammar)

for sentence in generate(grammar, n=5, depth=5): #grammar 문법에 맞는 것 생성 n은 문장의 수 , depth은 최대 다섯개의 규칙만 적용
    palindrome = "".join(sentence).replace(" ", "")
    print("Generated Word: {}, Size : {}".format(palindrome, len(palindrome)))
