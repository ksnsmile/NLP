#토큰화-NLTK 내장 토크나이저 사용법
#토큰화 : 더 작은 단위로 나누는 것 EX) 단어나 구두점으로 구분하는것 

from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

lTokenizer = LineTokenizer(); #줄 단위로 토큰화 실시
print("Line tokenizer output :",lTokenizer.tokenize("My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurelius. \nFather to a murdered son, husband to a murdered wife. \nAnd I will have my vengeance, in this life or the next."))

rawText = "By 11 o'clock on Sunday, the doctor shall open the dispensary."
sTokenizer = SpaceTokenizer() #공백을 기준으로 토큰화 실시
print("Space Tokenizer output :",sTokenizer.tokenize(rawText))

print("Word Tokenizer output :", word_tokenize(rawText)) #단어와 구두점이 구분된다.

tTokenizer = TweetTokenizer() #특수만주,해시태크,이모티콘, 특별 단어 등이 구분된다.
print("Tweet Tokenizer output :",tTokenizer.tokenize("This is a cooool #dummysmiley: :-) :-P <3"))
