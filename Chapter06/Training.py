#청커학습

import nltk
from nltk.corpus import conll2000

# =============================================================================
# IOB 태깅
# B-PER: 사람 이름(PERson)의 시작임을 나타냅니다.
# I-PER: 사람 이름 엔티티의 내부임을 나타냅니다.
# O: 어떤 엔티티에도 속하지 않음을 나타냅니다.
# =============================================================================


sentence = "Ravi is the CEO of a Company."


# 청커 규칙을 만든다 태깅 되어져 있는것을 기반으로 구를 찾는 것 규칙 정의
def myParser():
    grammar = '\n'.join([
	'NP: {<DT>*<NNP>}',
	'NP: {<JJ>*<NN>}',
	'NP: {<NNP>+}',
	])
    return nltk.RegexpParser(grammar)


# IOB태깅을 하는 것 
def buildIOBTags(text):
    chunkparser = myParser()
    words = nltk.word_tokenize(text)
    postags = nltk.pos_tag(words)
    tree = chunkparser.parse(postags)
    # This whole thing can be replaced by
    # nltk.chunk.tree2conlltags(tree) function
    # which returns 3 tuple
    return nltk.chunk.tree2conlltags(tree)
"""
    for subtree in tree:
	if type(subtree) is not tuple:
	    tokenPosition = 0
	    for token in subtree.leaves():
		if tokenPosition == 0:
		    print(' '.join([token[0], token[1], 'B-{}'.format(subtree.label())]))
		else:
		    print(' '.join([token[0], token[1], 'I-{}'.format(subtree.label())]))
		tokenPosition = tokenPosition + 1
	else:
	    token = subtree
	    print(' '.join([token[0], token[1], 'O']))
    """

#아무 규칙 없이 기본 청커의 성능을 평가하여 기준점 역할
def test_baseline():
    cp = nltk.RegexpParser("")
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP']) #conll2000 코퍼스의 test.txt 파일에서 명사구(NP)만 포함된 테스트 문장 집합을 가져
    # print(len(test_sents[0]))
    # print(test_sents[0])
    print(cp.evaluate(test_sents)) #구문 규칙 없이 기본 청커를 사용한 점수가 얼마인지 비교 목적으로 확인합니다.

#특정 정규 표현식 기반 규칙을 사용한 청커의 성능을 평가
def test_regexp():
    grammar = r"NP: {<[CDJNP].*>+}" #<[CDJNP].*>+: C, D, J, N, P로 시작하는 품사 태그를 가진 단어들이 1개 이상 연속으로 나타날 때 이를 **명사구(NP)**로 인식
    cp = nltk.RegexpParser(grammar)
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    print(cp.evaluate(test_sents))
    
#사용자 정의 구문 규칙을 적용한 청커의 성능을 평가
def test_myparser():
    parser = myParser()
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    print(parser.evaluate(test_sents))

class BigramChunker(nltk.ChunkParserI): #nltk.ChunkParserI를 상속
    def __init__(self, train_sents):
        #nltk.chunk.tree2conlltags(sent) 함수는 청크 트리 sent를 (단어, 품사, 청크 태그)의 형식으로 변환
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence): #입력: (단어, 품사) 형태의 튜플
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

def test_mychunker():
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    my_chunker = BigramChunker(train_sents)
    print(my_chunker.evaluate(test_sents))


#test_baseline()
#test_myparser()
test_regexp()
test_mychunker()

# =============================================================================
# 태거는 텍스트의 각 단어에 대해 품사(Part-of-Speech, POS) 태그를 부여하는 도구
# 청커는 태거가 부여한 품사 태그를 기반으로 문장 내 특정 구(Phrase)를 찾아내는 도구입니다. 
# 청커는 명사구(NP), 동사구(VP)와 같은 구문 단위로 문장을 나누는 역할 
# 태깅은 단어에 특정 태그를 부여하는 일반적인 작업을 의미
# 파서는 문장전체분석하는 것 청커는 특별한구 분석하는것 
# =============================================================================







