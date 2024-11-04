#정규표현식 -',+,?사용법

import re
def text_match(text, patterns):
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac", "ab?")) # '?' 는 'a' 뒤에 'b'가 0번 또는 1번 나올 수 있음
print(text_match("abc", "ab?"))
print(text_match("abbc", "ab?"))

print(text_match("ac", "ab*"))
print(text_match("abc", "ab*"))
print(text_match("abbc", "ab*")) # 'a' 뒤에 'b'가 0이상 

print(text_match("ac", "ab+")) # 'a' 뒤에 'b'가 1번 이상
print(text_match("abc", "ab+"))
print(text_match("abbc", "ab+"))

print(text_match("abbc", "ab{2}"))  # 'a' 뒤에 'b'가 정확히 2번 나와야 함
print(text_match("aabbbbbbc", "ab{3,5}?")) # 'a' 뒤에 'b'가 3~5번 나올 수 있음
