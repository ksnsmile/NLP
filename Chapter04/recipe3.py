#여러 개의 리터럴 문자열과 하위 문자열 검색

import re

#search for literal strings in sentence
patterns = [ 'Tuffy', 'Pie', 'Loki' ]
text = 'Tuffy eats pie, Loki eats peas!'
for pattern in patterns: # test에 있는 문장에서 pattern을 발견하면 found 대소문자 구분한다.
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Found!')
    else:
        print('Not Found!')

# =============================================================================
# search a substring and find it's location too
# %s: 문자열(string)
# %d: 정수(decimal)
# =============================================================================

text = 'Diwali is a festival of lights, Holi is a festival of colors!'
pattern = 'festival'
for match in re.finditer(pattern, text):  #위치 파악 
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))