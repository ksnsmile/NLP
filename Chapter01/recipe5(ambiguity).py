#모호한 단어를 가지고 워드넷을 사용해 모든 의미 탐구
#예를 들어 bat은 의미가 야구방망이, 박쥐 ,배트맨을 의미하기도 한다.
#워드넷은 단어들을 동의어 집합(synsets)으로 그룹화

from nltk.corpus import wordnet as wn

chair = 'chair'

chair_synsets = wn.synsets(chair) #워드넷 데이터 베이스에 들어가 chair 관련된 모든 뜻을 가져오는 api인터페이스이다.

#chair_synsets: 동의어 집합
print('Synsets/Senses of Chair :', chair_synsets, '\n\n')


#Lemmas(레머)는 단어의 기본 형태나 어근 // better"의 레머는 "good"

for synset in chair_synsets:
    print(synset, ': ')
    print('Definition: ', synset.definition())
    print('Lemmas/Synonymous words: ', synset.lemma_names())
    print('Example: ', synset.examples(), '\n')
