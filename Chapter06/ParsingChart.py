from nltk.grammar import CFG
from nltk.parse.chart import ChartParser, BU_LC_STRATEGY

grammar = CFG.fromstring("""
S -> T1 T4
T1 -> NNP VBZ
T2 -> DT NN
T3 -> IN NNP
T4 -> T3 | T2 T3
NNP -> 'Tajmahal' | 'Agra' | 'Bangalore' | 'Karnataka'
VBZ -> 'is'
IN -> 'in' | 'of'
DT -> 'the'
NN -> 'capital'
""")

cp = ChartParser(grammar, BU_LC_STRATEGY, trace=True) 

# =============================================================================
# BU_LC_STRATEGY는 바텀-업 (bottom-up) 방식의 로컬 제약 전략을 의미하며, 
# 파싱 시 작은 부분부터 시작해 전체 문장을 구성하는 방식입니다.
# trace=True는 파싱 과정의 각 단계를 추적할 수 있게 합니다.
# =============================================================================

#chartparser 차트를 기반으로 문장 파싱하는 것 

sentence = "Bangalore is the capital of Karnataka"
tokens = sentence.split()
chart = cp.chart_parse(tokens)
parses = list(chart.parses(grammar.start()))
print("Total Edges :", len(chart.edges()))
for tree in parses: print(tree)
tree.draw()
