#워드넷으로 명사,동사,형용사,부사의 다의어 평균 계산
#polysemy 다의성
from nltk.corpus import wordnet as wn
type = 'n'

#synsets 리스트에는 bank.n.01, bank.n.02와 같은 여러 동의어 집합이 포함됩니다.
synsets = wn.all_synsets(type)


# =============================================================================
# synset.lemmas()는 이 동의어 집합에 포함된 모든 기본형(단어)을 반환합니다.
# 즉,에는 위의 경우 ['bank', 'depository financial institution', 'banking company']라는 리스트가 반환됩니다.
# =============================================================================

lemmas = []
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())

print(len(lemmas))
lemmas = set(lemmas) #중복되는 것 제외 교유한 기본형의 수 
print('Total distinct lemmas: ', len(lemmas))

count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type)) #기본형이 가지는 의미의 수 

# =============================================================================
# lemma가 bank 면
# Synset('bank.n.01') : a financial institution that accepts deposits and makes loans
# Synset('bank.n.02') : the land alongside a body of water
# Synset('bank.n.03') : a slope in a road or path
# Synset('bank.n.04') : a supply or stock held in reserve for future use
# =============================================================================


print('Total senses :',count)
print('Average Polysemy of ', type,': ' ,  count/len(lemmas))
