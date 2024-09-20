from nltk.corpus import reuters # nltk라이브러리 다운하여 corpus모듈에서 reuters 객체 가져옴

files = reuters.fileids() # 특정말뭉치 객체를 가져와서 파일로 변환

worlds16097=reuters.words(['test/16097']) # 상대경로 파일을 word로 정의

worlds20=reuters.words(['test/16097'])[:20] # 20개만 추출

reutersGenres=reuters.categories() #로이터 안에 있는 장르 추출

for w in reuters.words(categories=['bop','cocoa']):
    print(w+' ',end='')
    if(w is '.'):
        print()