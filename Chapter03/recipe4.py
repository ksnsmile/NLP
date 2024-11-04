#불용어 - 불용어 말뭉치 사용법과 불용어가 만들어내는 차이점 확인 

import nltk
from nltk.corpus import gutenberg
print(gutenberg.fileids())

gb_words = gutenberg.words('bible-kjv.txt')
words_filtered = [e.lower() for e in gb_words if len(e) >= 3]
stopwords = nltk.corpus.stopwords.words('english') #불용어에서 영어 부분을 가져온다
words = [w for w in words_filtered if w.lower() not in stopwords]

fdist = nltk.FreqDist(words) #불용어를 제거한 단어 리스트
fdist2 = nltk.FreqDist(gb_words) #불용어를 제거하지 않은 단어 리스트


print('Following are the most common 10 words in the bag')
print(fdist2.most_common(10))
print('Following are the most common 10 words in the bag minus the stopwords')
print(fdist.most_common(10))
fdist.plot()