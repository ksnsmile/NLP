#시프트 변환 구문 분석

#밑에서 위로
# =============================================================================
# 스택과 입력 큐를 사용하여 상향식-하향식 결합 방식으로 분석
# 
# 장점: 결정적인 방식으로 간단하고 빠름
# 단점: 복잡한 문장 구조에 약함
# =============================================================================

import nltk

def SRParserExample(grammar, textlist):
    parser = nltk.parse.ShiftReduceParser(grammar)
    for text in textlist:
        sentence = nltk.word_tokenize(text)
        for tree in parser.parse(sentence):
            print(tree)
            tree.draw()

text = [
    "Tajmahal is in Agra",
    "Bangalore is the capital of Karnataka",
]

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

SRParserExample(grammar, text)
