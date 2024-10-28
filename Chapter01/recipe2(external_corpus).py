#외부 말뭉치 다운로드,로드하고 액세스하기

from nltk.corpus import CategorizedPlaintextCorpusReader #이미 분류되어져있는 것을 가져오는것 


reader = CategorizedPlaintextCorpusReader(r"C:\Users\ksn71\OneDrive\바탕 화면\git\NLP\datasets\mix20_rand700_tokens_cleaned\tokens", r'.*\.txt', cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids())

posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')

from random import randint

fileP = posFiles[randint(0,len(posFiles)-1)]
fileN = negFiles[randint(0, len(posFiles) - 1)]
print(fileP)
print(fileN)


for w in reader.words(fileP):
    print(w + ' ', end='')
    if (w is '.'):
        print()


for w in reader.words(fileN):
    print(w + ' ', end='')
    if (w is '.'):
        print()
        
       