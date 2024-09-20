import nltk
from nltk.corpus import brown

# 브라운 코퍼스를 다운로드 (최초 1회만 필요)
nltk.download('brown')

# 브라운 코퍼스의 카테고리 출력
print(brown.categories())

genres=['fiction','humor','romance']
whwords=['what','which','how','why','when','where','who']

for i in range(0,len(genres)):
    genre=genres[i]
    print()
    print("'"+genre+"' wh단어 분석")
    genre_text=brown.words(categories=genre)

fdist=nltk.FreqDist(genre_text)

for wh in whwords:
    print(wh + ':', fdist[wh],end=' ')