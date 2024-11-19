#간다한 청커 작성

import nltk

text = "Ravi is the CEO of a Company. He is very powerful public speaker also."

grammar = '\n'.join([
    'NP: {<DT>*<NNP>}',  #<DT>*: 관사(Determiner) 태그가 0개 이상 올 수 있다.,<NNP>: 고유 명사(Singular Proper Noun)
    'NP: {<JJ>*<NN>}',  # 형용사0개이상 + 명사
    'NP: {<NNP>+}', # 명사 1개 이상
])

sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunkparser = nltk.RegexpParser(grammar)
    result = chunkparser.parse(tags)
    print(result)
