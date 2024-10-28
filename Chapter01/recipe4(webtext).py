#웹 및 채팅 텍스트 자료 파일 중 하나에서 빈도 분포 찾기
import nltk 

from nltk.corpus import webtext
print(webtext.fileids())

fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_words)

print('Count of the maximum appearing word "',fdist.max(),'" : ', fdist[fdist.max()])
print('Total Number of distinct tokens in the bag : ', fdist.N())
print('Following are the most common 10 words in the bag')
print(fdist.most_common(10))
print('Frequency Distribution on Personal Advertisements')
print(fdist.tabulate())
fdist.plot(cumulative=True)


#막상 가장 많이 쓰이는 단어를 10개를 추출해도 의미가 크게 없다 왜냐하면 불용어 처리를 해주지 않았기 때문이다.