# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:44:21 2024

@author: ksn71
"""

from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer

raw="My name is Maximus Decimus Meridus, commander of the Armies of the North,\
        General of the Felix Legions and loyal servant to the true emperor,\
        Marcus Aurelius. \nFather to a murdered son, husband to a murdered wife.\
            \nAnd I will have my vengeance, in this life or the next."
                                                    
                                                    
tokens=word_tokenize(raw)


#어간 추출 (Stemming)
porter=PorterStemmer()
stems=[porter.stem(t) for t in tokens]
print(stems)

#표제어 추출 (Lemmatization) _ 사전에 있는 것을 mapping 하는 것 better to good 
lemmatizer=WordNetLemmatizer()
lemmas=[lemmatizer.lemmatize(t) for t in tokens]
print(lemmas)