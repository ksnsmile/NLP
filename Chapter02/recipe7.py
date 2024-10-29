#BeautifulSoup를 사용한 HTML 파싱

from bs4 import BeautifulSoup

html_doc = open('sample-html.html', 'r').read() #html파일의 내용을 str 객체로 불러온다.
soup = BeautifulSoup(html_doc, 'html.parser')

print('Full text HTML Stripped:')
print(soup.get_text()) #htmp이 제거된 내용

print('Accessing the <title> tag :', end=' ')
print(soup.title) #첫번째 title 태그 반환

print('Accessing the text of <H1> tag :', end=' ')
print(soup.h1.string) #h1태그에 둘러싸인 텍스트 반환

print('Accessing property of <img> tag :', end=' ')
print(soup.img['alt']) #이미지 태그의 alt속성에 액세스

print('\nAccessing all occurences of the <p> tag :')
for p in soup.find_all('p'): #<p>태그에 걸리는 모든 테스트를 반환 하는 것 
    print(p.string)
    
# =============================================================================
# HTML: 웹 페이지를 만들기 위한 언어로, 주로 콘텐츠의 구조와 표현을 정의합니다. 
# HTML은 웹 브라우저에서 표시될 내용을 위한 마크업을 제공합니다.
# 
# XML: 데이터의 구조와 저장을 위한 언어로, 데이터의 의미와 구조를 정의하는 데 중점을 둡니다. 
# XML은 데이터를 쉽게 전송하고 저장할 수 있도록 설계되었습니다.
# =============================================================================
