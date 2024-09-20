# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:30:41 2024

@author: ksn71
"""

from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer # 줄로 나누기,
from nltk import word_tokenize


lTokenizer=LineTokenizer()
print("Line tokenizer 출력 : ", lTokenizer.tokenize("My name is Maximus Decimus Meridus, commander of the Armies of the North,\
                                                 General of the Felix Legions and loyal servant to the true emperor,\
                                                Marcus Aurelius. \nFather to a murdered son, husband to a murdered wife.\
                                                    \nAnd I will have my vengeance, in this life or the next."))
                                                    
                                                    
rawText="By 11 o'clock on Sunday, the doctor shall open the dispensary."
sTtokenizer=SpaceTokenizer() # 공백문자로 나누어서 함
print("Space Tokenizer 출력 :",sTtokenizer.tokenize(rawText))
                                                
print("Word Tokenizer 출력 : ", word_tokenize(rawText)) # 단어자체 그리고 구두점 까지

tTokenizer=TweetTokenizer()
print("Tweet Tokenizer 출력 : ",tTokenizer.tokenize("This is a cooool #dummysmiley: :-) :-p <3"))



