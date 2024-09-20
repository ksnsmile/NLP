from nltk.corpus import CategorizedPlaintextCorpusReader

reader = CategorizedPlaintextCorpusReader(r'C:/Users/ksn71/OneDrive/바탕 화면/git/NLP/pythonProject/mix20_rand700_tokens_cleaned/tokens'
                                         , r'.*\.txt',cat_pattern=r'(\w+)/*')

print(reader.categories()) #카테고리 출력

print(reader.fileids()) #파일이름 출력

posFiles=reader.fileids(categories='pos')
negFiles=reader.fileids(categories='neg')

from random import randint
fileP=posFiles[randint(0,len(posFiles)-1)]
fileN=negFiles[randint(0,len(posFiles)-1)]
print(fileP)
print(fileN)

for w in reader.words(fileP):
    print(w+' ',end='')
    if (w is '.'):
        print()

for w in reader.words(fileN):
    print(w+' ',end='')
    if(w is '.'):
        print()