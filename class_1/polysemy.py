from nltk.corpus import wordnet as wn #lemmas는 동의어 auto, car 등
type='n'

synsets=wn.all_synsets(type)

lemmas=[]
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())

lemmas=set(lemmas)

count=0
for lemma in lemmas:
    count=count+len(wn.synsets(lemma, type))

print('개별 기본형 합계: ', len(lemmas))
print('총 뜻: ', count)
print(type, '(명사)의 다의어 평균: ',count/len(lemmas))
