#재귀 하향 구문 분석

#위에서 밑으로 분석
# =============================================================================
# 재귀적 규칙 적용으로 하향식 방식으로 분석
# 장점: 백트래킹으로 복잡한 문장 구조도 분석 가능
# 단점: 백트래킹으로 인해 속도가 느려질 수 있음
# =============================================================================

import nltk

def RDParserExample(grammar, textlist):
    #RecursiveDescentParser는 문법 규칙에 맞는 문장의 구문 구조를 분석하고 구문 트리(parse tree)를 생성
    parser = nltk.parse.RecursiveDescentParser(grammar)
    for text in textlist:
        sentence = nltk.word_tokenize(text)
        for tree in parser.parse(sentence):
            print(tree)
            tree.draw()

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NNP VBZ
VP -> IN NNP | DT NN IN NNP
NNP -> 'Tajmahal' | 'Agra' | 'Bangalore' | 'Karnataka'
VBZ -> 'is'
IN -> 'in' | 'of'
DT -> 'the'
NN -> 'capital'
""")

text = [
    "Tajmahal is in Agra",
    "Bangalore is the capital of Karnataka",
]

RDParserExample(grammar, text)
