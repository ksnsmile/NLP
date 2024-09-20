# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PyPDF2 import PdfReader

def getTextPDF(pdfFileName,password=''):
    
    pdf_file=open(pdfFileName,'rb')
    read_pdf=PdfReader(pdf_file)
    
    if password != '':
        read_pdf.decrypt(password)
        
        text=[]
        
        for i in range(0,read_pdf.getNumPages()-1):
            text.append(read_pdf.getPage(i).extractText())
            
        
        
        return '\n'.join(text)
    
    