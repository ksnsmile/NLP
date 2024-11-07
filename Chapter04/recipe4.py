#날짜 정규표현식과 문자 집합 또는 문자 범위 집합 만들기
#regex : 정규표현식(특정 패턴을 가진 문자열을 찾거나 처리하기 위해 사용하는 표현식)
import re

# =============================================================================
# (\d{4}): 네 자리 숫자. 일반적으로 연도를 나타냅니다.
# /(\d{1,2}): 슬래시 뒤에 나오는 한 자리 또는 두 자리 숫자. 보통 월을 나타냅니다.
# /(\d{1,2}): 다시 슬래시 뒤에 나오는 한 자리 또는 두 자리 숫자. 일자를 나타냅니다.
# =============================================================================

url= "http://www.telegraph.co.uk/formula-1/2017/10/28/mexican-grand-prix-2017-time-does-start-tv-channel-odds-lewis1/2017/05/12/"
date_regex = '/(\d{4})/(\d{1,2})/(\d{1,2})/'

print("Date found in the URL :", re.findall(date_regex, url,flags=0)) #flags=0은 대소문자 구별 안 하는 것 ,모든 일치를 찾는것 findall()


# 특정문자가 있는지 확인하는 함수 생성

def is_allowed_specific_char(string): 
    #정규 표현식 정의
    #대괄호 안에 ^가 있으면 "괄호 안의 문자가 아닌" 문자를 의미 
    # r'[^a-zA-Z0-9.]'은 알파벳 대소문자(a-z, A-Z), 숫자(0-9), 점(.)을 제외한 문자
    charRe = re.compile(r'[^a-zA-Z0-9.]') 
    
    # 특정표현식 있는지 찾기 있으면 매칭된 객체 받게됨
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450."))
print(is_allowed_specific_char("*&%@#!}{"))
