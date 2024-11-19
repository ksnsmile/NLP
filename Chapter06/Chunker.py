#내장 청커 사용

# 청킹: 텍스트에서 짧은 구를 추출하는 것

import nltk

text = "Lalbagh Botanical Gardens is a well known botanical garden in Bengaluru, India."
sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(tags) #품사태깅 된것에서 그것이 지역이냐 사람이냐 등을 판별해주는 것 
    print(chunks)
