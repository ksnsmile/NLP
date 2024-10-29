from PyPDF2 import PdfFileReader

def getTextPDF(pdfFileName, password = ''):
    pdf_file = open(pdfFileName, 'rb') #바이너리모드에서 파일 열기
    read_pdf = PdfFileReader(pdf_file)
    if password != '':
        read_pdf.decrypt(password) #암호해제 
    text = []
    for i in range(0,read_pdf.getNumPages()): #PDF 페이지수를 반환
        text.append(read_pdf.getPage(i).extractText())
    return '\n'.join(text)