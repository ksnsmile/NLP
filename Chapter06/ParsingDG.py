#의존 문법과 투사 의존성 구문 분석

import nltk

grammar = nltk.grammar.DependencyGrammar.fromstring("""
'savings' -> 'small'
'yield' -> 'savings'
'gains' -> 'large'
'yield' -> 'gains'
""")

sentence = 'small savings yield large gains'
dp = nltk.parse.ProjectiveDependencyParser(grammar)
for t in sorted(dp.parse(sentence.split())):
    print(t)
    t.draw()
