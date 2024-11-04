# 스테밍-NLTK 내장 스테머 사용법
# 어간(stem) 스테밍(어간추출) 어간은 접미사가 없는 기본형
#먼저 토큰화를 실시하고 어간추출해야해서 순서가 이렇게 되는 것 
from nltk import PorterStemmer, LancasterStemmer, word_tokenize

raw = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

porter = PorterStemmer() # 어간 추출 하는 것 
pStems = [porter.stem(t) for t in tokens]
print(pStems)

lancaster = LancasterStemmer() #좀 더 많이 제거한다.
lStems = [lancaster.stem(t) for t in tokens]
print(lStems)