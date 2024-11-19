#내장 개체명 인식 기능 사용 

#NER(Named Entity Recognition) 고유명사 찾는 것 
import nltk

def sampleNE():
    #품사 태그가 붙은 문장들로 구성되어 있고, 각 문장은 (단어, 품사태그) 튜플의 리스트입니다.
    sent = nltk.corpus.treebank.tagged_sents()[0]
    #함수는 문장에서 명명된 개체(Named Entity)를 인식하여 이를 트리 구조로 반환합니다
    print(nltk.ne_chunk(sent))

def sampleNE2():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    #단지 "개체명"과 "비개체명"으로 구분됩니다. 이는 개체명을 간단하게 이진 분류로 처리하는 방식입니다
    print(nltk.ne_chunk(sent, binary=True))

if __name__ == '__main__':
    sampleNE()
    sampleNE2()
