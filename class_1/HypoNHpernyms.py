from nltk.corpus import wordnet as wn  #synset 는 그 단어의 동의어 예문 등을 다 모아둔것

woman=wn.synset('woman.n.01')

bed=wn.synset('bed.n.01')

print(woman.hypernyms())

woman_paths=woman.hypernym_paths()

for idx,path in enumerate(woman_paths): # 상위어 경로 알아 보는 것 (woman의)
    print('\n\n상위어 경로 :',idx+1)
for synset in path:
    print(synset.name(), ', ', end='')

types_of_beds=bed.hyponyms()
print('\n\nbed의 형태(하위어): ',types_of_beds)

print(sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas())))