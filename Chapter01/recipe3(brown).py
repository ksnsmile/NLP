#브라운 코퍼스에서 세 가지 장르의 wh단어 모두 세기
import nltk
from nltk.corpus import brown 

print(brown.categories())

genres = ['fiction', 'humor', 'romance']
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']



# 각 장르별로 whwords의 값이 몇개 있는지 알려주는 코드 
for i in range(0,len(genres)):
    genre = genres[i]
    print()
    print("Analysing '"+ genre + "' wh words")
    genre_text = brown.words(categories = genre)
    fdist = nltk.FreqDist(genre_text)
    for wh in whwords:
        print(wh + ':', fdist[wh], end=' ')
