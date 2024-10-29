#PDF,DOCX, 일반 텍스트 파일을 가져와 사용자 정의 말뭉치 생성

import os
import word, pdf
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

def getText(txtFileName):
    file = open(txtFileName, 'r')
    return file.read()

newCorpusDir = 'mycorpus/'
if not os.path.isdir(newCorpusDir):
    os.mkdir(newCorpusDir)

txt1 = getText('sample_feed.txt')
txt2 = pdf.getTextPDF('sample-pdf.pdf')
txt3 = word.getTextWord('sample-one-line.docx')

# mycorpus/파일에 추가로 파일 생성 하는 것 거기다가 글 쓰기 
files = [txt2,txt3]
for idx, f in enumerate(files):
    with open(newCorpusDir+str(idx)+'.txt', 'w') as fout:
        fout.write(f)

newCorpus = PlaintextCorpusReader(newCorpusDir, '.*') #새로운 말뭉치 객체 생성 

print(newCorpus.words())
print(newCorpus.sents(newCorpus.fileids()[1])) #문장들의 리스트 출력 
print(newCorpus.paras(newCorpus.fileids()[0])) # 문다들의 리스트 출력 
