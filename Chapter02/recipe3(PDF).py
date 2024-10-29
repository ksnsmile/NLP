#파이썬에서 PDF 파일 읽기 

import pdf

pdfFile = 'sample-one-line.pdf'
pdfFileEncrypted = 'sample-one-line.protected.pdf'

print('PDF 1: \n',pdf.getTextPDF(pdfFile)) #PDF 글 가져오기 
print('PDF 2: \n',pdf.getTextPDF(pdfFileEncrypted,'tuffy')) #암호가 걸려있을 경우 사용 
