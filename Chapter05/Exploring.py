#내장 태거 탐구

#태깅은 품사를 사용하여 주어진 문장의 단어를 분류하는 프로세스이다.
#즉 품사 태그를 달아주는 역할을 한다.
import nltk
simpleSentence = "Bangalore is the capital of Karnataka."
wordsInSentence = nltk.word_tokenize(simpleSentence)
print(wordsInSentence)
partsOfSpeechTags = nltk.pos_tag(wordsInSentence)
print(partsOfSpeechTags)
