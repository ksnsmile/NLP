# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:36:31 2024

@author: ksn71
"""

import os
import word,pdf

from nltk.corpus.reader.plaintext import PlaintextCorpusReader

def getText(txtFileName):
    file=open(txtFileName,'r')
    return file.read()


newCorpusDir='mycorpus/'
if not os.path.isdir(newCorpusDir):
    os.mkdir(newCorpusDir)
    
    
txt1=getText('sample_feed.txt')

txt2=pdf.getText('sample-pdf.pdf')

txt3=word.getTextWord('sample-one-line.docx')

files=[txt1,txt2,txt3]
for idx,f in enumerate(files):
    with open(newCorpusDir+str(idx)+'.txt','w') as fout:
        fout.write(f)
        
newCorpusDir=PlaintextCorpusReader(newCorpusDir, '.*')

print(newCorpusDir.words()) # 그냥 단어
print(newCorpusDir.sents(newCorpusDir.files()[1])) #문장단위
print(newCorpusDir.paras(newCorpusDir.files()[0])) # 문단단위
























