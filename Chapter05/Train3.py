#자체 태거 학습

import nltk
import pickle

def sampleData():
    return [
        "Bangalore is the capital of Karnataka.",
        "Steve Jobs was the CEO of Apple.",
        "iPhone was Invented by Apple.",
        "Books can be purchased in Market.",
    ]

def buildDictionary():
    dictionary = {}
    for sent in sampleData():
        partsOfSpeechTags = nltk.pos_tag(nltk.word_tokenize(sent))
        for tag in partsOfSpeechTags:
            value = tag[0]
            pos = tag[1]
            dictionary[value] = pos
    return dictionary

#태거 객체를 저장하는 함수
def saveMyTagger(tagger, fileName):
    fileHandle = open(fileName, "wb")
    pickle.dump(tagger, fileHandle)
    fileHandle.close()

# 학습시키는것 buildDictionary는 학습데이터를 지도방식으로 보여주고 unigramtagger가 학습하는 모델임.

def saveMyTraining(fileName):
    tagger = nltk.UnigramTagger(model=buildDictionary())
    saveMyTagger(tagger, fileName)


def loadMyTagger(fileName):
    return pickle.load(open(fileName, "rb"))

sentence = 'Iphone is purchased by Steve Jobs in Bangalore Market'
fileName = "myTagger.pickle"

saveMyTraining(fileName)

myTagger = loadMyTagger(fileName)

print(myTagger.tag(nltk.word_tokenize(sentence)))
