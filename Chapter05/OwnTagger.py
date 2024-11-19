#자체 태거 작성

import nltk
def learnDefaultTagger(simpleSentence):
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    tagger = nltk.DefaultTagger("NN") #NN이라고 기본단어에 붙인다.
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)
    
# 가르쳐 준것을 토대로 하는 태깅하는 것 
def learnRETagger(simpleSentence):
    customPatterns = [
        (r'.*ing$', 'ADJECTIVE'),             # running: 형용사
        (r'.*ly$', 'ADVERB'),                 # willingly :부사
        (r'.*ion$', 'NOUN'),                  # intimation: 명사
        (r'(.*ate|.*en|is)$', 'VERB'),        # terminate, darken, lighten :동사
        (r'^an$', 'INDEFINITE-ARTICLE'),      # terminate :관사
        (r'^(with|on|at)$', 'PREPOSITION'),   # on :전치사
        (r'^\-?[0-9]+(\.[0-9]+)$', 'NUMBER'), # -1.0, 12345.123 :숫자
        (r'.*$', None),
    ]
    tagger = nltk.RegexpTagger(customPatterns)
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)
    
# 지정한 품사로 태깅하는것 
def learnLookupTagger(simpleSentence):
    mapping = {
        '.': '.', 'place': 'NN', 'on': 'IN',
        'earth': 'NN', 'Mysore' : 'NNP', 'is': 'VBZ',
        'an': 'DT', 'amazing': 'JJ'
    }
    tagger = nltk.UnigramTagger(model=mapping)
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)

if __name__ == '__main__':
    testSentence = "Mysore is an amazing place on earth. I have visited Mysore 10 times."
    learnDefaultTagger(testSentence)
    learnRETagger(testSentence)
    learnLookupTagger(testSentence)
