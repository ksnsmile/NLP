#두 개의 구별되는 동의어 집합을 선택하고 워드넷을 사용해 상위어와 하위어 개념 탐색

from nltk.corpus import wordnet as wn

woman = wn.synset('woman.n.01')
bed = wn.synset('bed.n.01')

print(woman.hypernyms()) #상위어
woman_paths = woman.hypernym_paths()

for idx, path in enumerate(woman_paths): # woman_path에서 어떻게 위에서 woman까지 오게됬는지 과정을 보여주는 코드
    print('\n\nHypernym Path :', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end='')


# =============================================================================
# "bed"의 하위어에서 고유한 어근을 추출하고, 그 중복을 제거한 후 정렬하여 출력하게 됩니다. 
# 따라서, "bed"와 관련된 다양한 침대의 종류를 고유한 형태로 알 수 있게 됩니다.
# =============================================================================

types_of_beds = bed.hyponyms() #하위어 //하위어는 모호하지가 않다.
print('\n\nTypes of beds(Hyponyms): ', types_of_beds)

print(sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas()))) 


