#분류기를 사용한 문장 분할

# =============================================================================
# 학습 데이터를 기반으로 마침표가 문장의 끝인지 여부를 예측하는 분류기를 학습.
# 테스트 데이터를 분류기를 사용해 문장 단위로 분리.
# =============================================================================

import nltk

# 마침표 바로 다음이 대문자인지 확인하는 것 
def featureExtractor(words, i):
    return ({'current-word': words[i], 'next-is-upper': words[i+1][0].isupper()}, words[i+1][0].isupper())

# 특징과 레이블을 출력 
# 예:({'current-word': '.', 'next-is-upper': True}, True)
def getFeaturesets(sentence):
    words = nltk.word_tokenize(sentence)
    featuresets = [featureExtractor(words, i) for i in range(1, len(words) - 1) if words[i] == '.']
    return featuresets

def segmentTextAndPrintSentences(data):
    words = nltk.word_tokenize(data)
    for i in range(0, len(words) - 1):
        if words[i] == '.':
            if classifier.classify(featureExtractor(words, i)[0]) == True:
                print(".")
            else:
                print(words[i], end='') #이어져 나오게 하는 것 
        else:
            print("{} ".format(words[i]), end='')
    print(words[-1])
# copied the text from https://en.wikipedia.org/wiki/India
traindata = "India, officially the Republic of India (Bhārat Gaṇarājya),[e] is a country in South Asia. it is the seventh-largest country by area, the second-most populous country (with over 1.2 billion people), and the most populous democracy in the world. It is bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast. It shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the northeast; and Myanmar (Burma) and Bangladesh to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives. India's Andaman and Nicobar Islands share a maritime border with Thailand and Indonesia."
testdata = "The Ind.ian subcontinent was home to the urban Indus Valley Civilisation of the 3rd millennium BCE. In the following millennium, the oldest scriptures associated with Hinduism began to be composed. Social stratification, based on caste, emerged in the first millennium BCE, and Buddhism and Jainism arose. Early political consolidations took place under the Maurya and Gupta empires; the later peninsular Middle Kingdoms influenced cultures as far as southeast Asia. In the medieval era, Judaism, Zoroastrianism, Christianity, and Islam arrived, and Sikhism emerged, all adding to the region's diverse culture. Much of the north fell to the Delhi sultanate; the south was united under the Vijayanagara Empire. The economy expanded in the 17th century in the Mughal Empire. In the mid-18th century, the subcontinent came under British East India Company rule, and in the mid-19th under British crown rule. A nationalist movement emerged in the late 19th century, which later, under Mahatma Gandhi, was noted for nonviolent resistance and led to India's independence in 1947."

traindataset = getFeaturesets(traindata)
classifier = nltk.NaiveBayesClassifier.train(traindataset)
segmentTextAndPrintSentences(testdata)
