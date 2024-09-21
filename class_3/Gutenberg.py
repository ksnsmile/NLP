# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:15:33 2024

@author: ksn71
"""
#불용어 없애기 ("이", "그", "그리고", "있다", "없다")
import nltk
nltk.download('stopwords')
from nltk.corpus import gutenberg

print(gutenberg.fileids())

gb_words=gutenberg.words('bible-kjv.txt')
words_filtered=[e for e in gb_words if len(e) >=3 ]

stopwords=nltk.corpus.stopwords.words('english')
words=[ w for w in words_filtered if w.lower() not in stopwords ]

fdistPlain=nltk.FreqDist(words)
fdist=nltk.FreqDist(gb_words)

print('Followig are the most common 10 words in the bag')
print(fdist.most_common(10))
print('Following are the most common 10 words in the bag minus the stopwords')
print(fdistPlain.most_common(10))

