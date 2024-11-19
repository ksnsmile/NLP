#NLP 파이프라인 생성 

#Threading은 컴퓨터 프로그램에서 여러 작업을 동시에 실행할 수 있도록 하는 프로그래밍 기술 
import nltk
import threading
import queue #대기열 라이브러리
import feedparser
import uuid

threads = []
queues = [queue.Queue(), queue.Queue()] #첫번째 대기열은 토큰화된 문장 저장, 두번쨰는 분석된 모든 품사 단어 저장

def extractWords():
    url = 'https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms'
    feed = feedparser.parse(url)
    for entry in feed['entries'][:5]:
        text = entry['title']
        if 'ex' in text:
            continue
        words = nltk.word_tokenize(text)
        data = {'uuid': uuid.uuid4(), 'input': words} #고유 아이디와 단어들 넣음 
        queues[0].put(data, True)
        print(">> {} : {}".format(data['uuid'], text))

def extractPOS():
    while True:
        if queues[0].empty(): # 첫번쨰 대기열이 비어있는지 확인
            break
        else:
            data = queues[0].get()
            words = data['input']
            postags = nltk.pos_tag(words)
            queues[0].task_done() #첫번째 대기열에서 작업이 끝났다는 것을 알림
            queues[1].put({'uuid': data['uuid'], 'input': postags}, True)

def extractNE():
    while True:
        if queues[1].empty():
            break
        else:
            data = queues[1].get()
            postags = data['input']
            queues[1].task_done()
            chunks = nltk.ne_chunk(postags, binary=False)
            print("  << {} : ".format(data['uuid']), end = '')
            
            #chunks 는 트리구조이므로 각 path에서 개체명 따오기
            for path in chunks:
                try:
                    label = path.label()
                    print(path, end=', ')
                except:
                    pass
            print()

def runProgram():
    e = threading.Thread(target=extractWords())
    e.start()
    threads.append(e)

    p = threading.Thread(target=extractPOS())
    p.start()
    threads.append(p)

    n = threading.Thread(target=extractNE())
    n.start()
    threads.append(n)

    queues[0].join()
    queues[1].join()

    for t in threads:
        t.join()

if __name__ == '__main__':
    runProgram()
