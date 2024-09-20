# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:00:02 2024

@author: ksn71
"""
import docx

def getTextWord(wordFileName):
    
    doc=docx.Document(wordFileName)
    
    fullText=[]
    for para in doc.paragraphs:
        fullText.append(para.text)
        
        
    return '\n'.join(fullText)



