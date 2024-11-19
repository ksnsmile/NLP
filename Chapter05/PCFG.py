#확률적 문맥 무관 문법 - CFG 작성
#터미널은 더 이상 분해할 수 없는 기호 예를 들어, 숫자 '0', 문자 'a', 'b', 'c' 등은 터미널입니다.
#비터미널은 규칙을 설명하는 기호 WORD는 LETTER NUMBER 또는 NUMBER LETTER
import nltk
from nltk.parse.generate import generate

productions = [
    "ROOT -> WORD [1.0]", #ROOT 는 WORD로 시작 할 확률이 1이다.
    "WORD -> P1 [0.25]", #WORD는 P1나올 확률이 0.25이다.
    "WORD -> P1 P2 [0.25]",
    "WORD -> P1 P2 P3 [0.25]",
    "WORD -> P1 P2 P3 P4 [0.25]",
    "P1 -> 'A' [1.0]",
    "P2 -> 'B' [0.5]",
    "P2 -> 'C' [0.5]",
    "P3 -> 'D' [0.3]",
    "P3 -> 'E' [0.3]",
    "P3 -> 'F' [0.4]",
    "P4 -> 'G' [0.9]",
    "P4 -> 'H' [0.1]",
]


#문법에서 WORD 는 한 번 확장 되면 고정

grammarString = "\n".join(productions)

grammar = nltk.PCFG.fromstring(grammarString)

print(grammar)

for sentence in generate(grammar, n=10, depth=5):
    palindrome = "".join(sentence).replace(" ", "")
    print("String : {}, Size : {}".format(palindrome, len(palindrome)))
