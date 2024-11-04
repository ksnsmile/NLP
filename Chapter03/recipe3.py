#원형 복원-NLTK WordnetLemmatizer 사용법 (어간 추출하면서 제거가 많이 되어서 원형 복원 작업 실시)

from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer

raw = "My name is Maximus Decimus Meridius, commander of the armies of the north, General of the Felix legions and loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

#어간 추출 
porter = PorterStemmer()
stems = [porter.stem(t) for t in tokens]
print(stems)


# 단어를 그 기본형으로 변환

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(t) for t in tokens]
print(lemmas)