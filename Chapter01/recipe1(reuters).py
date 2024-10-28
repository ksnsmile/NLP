#내장 말뭉치 액세스

from nltk.corpus import reuters #로이터 말뭉치

files = reuters.fileids() #로이터코퍼스에 있는 파일 경로 가져옴
print(files)

words16097 = reuters.words(['test/16097']) #그 파일에 있는 단어 가져옴
print(words16097)

words20 = reuters.words(['test/16097'])[:20]
print(words20)


reutersGenres = reuters.categories() #로이터에 있는 범주들을 뽑아내기
print(reutersGenres)


#로이터에 있는 bop,cocoa 범주에 있는 단어들을 전부 가져오기
for w in reuters.words(categories=['bop','cocoa']):
    print(w+' ',end='')
    if(w is '.'):
        print()
