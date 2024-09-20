# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:33:10 2024

@author: ksn71
"""
# 어간 추출 도구

from nltk import PorterStemmer, LancasterStemmer,word_tokenize

raw="My name is Maximus Decimus Meridius, commander of the Armies of the North,\
     General of the Felix Legions and loyal servant to the true emperor,\
          Marcus Aureliu. Father to a murdered son, husband to a murdered wife.\
              And I will have my vengeance, in this life or the next."
              
tokens=word_tokenize(raw)

porter=PorterStemmer() #보수적이어서 정확하게 끌어냄
pStems=[porter.stem(t) for t in tokens]
print(pStems)

lancaster = LancasterStemmer() # 속도가 빠름 대용량 처리 할 때 좋음
lStems=[lancaster.stem(t) for t in tokens]
print(lStems)