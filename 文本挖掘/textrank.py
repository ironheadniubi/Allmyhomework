from collections import defaultdict
from jieba.analyse.tfidf import KeywordExtractor
import jieba.posseg
import sys
from operator import itemgetter
class UndirectWeightedGraph:
    d = 0.85
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,start,end,weight):
        # use a tuple(start,end,weight) instead of a Edge object
        self.graph[start].append((start,end,weight))
        self.graph[end].append((end,start,weight))
    def rank(self):
        ws = defaultdict(float)
        outSum = defaultdict(float)
        wsdef = 1.0/(len(self.graph) or 1.0)
        for n,out in self.graph.items():
            ws[n]=wsdef
            for e in out:
                outSum[n]=sum((e[2] for e in out),0.0)
        # this line for build stable iteration
        sorted_keys=sorted(self.graph.keys())
        for x in range(10):
            for n in sorted_keys:
                s = 0
                for e in self.graph[n]:
                    s += (e[2]*ws[e[1]])/(outSum[e[1]])
                ws[n]=(1-self.d)+self.d*s
        (min_rank,max_rank) = (sys.float_info[0],sys.float_info[3])
       # print(min_rank,max_rank)
        for w in ws.values():
            if w<min_rank:
                min_rank = w
            if w>max_rank:
                max_rank = w
        for n,w in ws.items():
            # we can also choose *100 but this way is better
            ws[n]=(w-min_rank/10.0)/(max_rank-min_rank/10.0)

        return ws
# g = UndirectWeightedGraph()
# g.addEdge('a','b',3)
# g.addEdge('a','c',2)
# g.rank()

class TextRank(KeywordExtractor):
    def __init__(self):
        self.tokenizer = self.postokenizer=jieba.posseg.dt
        self.stop_words = self.STOP_WORDS.copy()
       # print(self.stop_words)
        self.pos_filt = frozenset(('ns','n','vn','v'))
        self.span = 5
    #get 名词,动词,名动词,地名
    def pairfilter(self,wp):
        return (wp.flag in self.pos_filt and len(wp.word.strip())>=2 and wp.word.lower() not in self.stop_words)

    def textrank(self, sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'), withFlag=False):
        self.pos_filt = frozenset(allowPOS)
        g=UndirectWeightedGraph()
        cm = defaultdict(int)
        words = tuple(self.tokenizer.cut(sentence))
        #print(type(words))
        #print(type(words[0]))
        for i,wp in enumerate(words):
            if self.pairfilter(wp):
                for j in range(i+1,i+self.span):
                    if j>=len(words):
                        break
                    if not self.pairfilter(words[j]):
                        continue
                    if allowPOS and withFlag:
                        cm[(wp,words[j])]+=1
                    else:
                        cm[(wp.word,words[j].word)]+=1
        for terms,w in cm.items():
            g.addEdge(terms[0],terms[1],w)
        nodes_rank = g.rank()
      #  print(nodes_rank.items())
        if withWeight:
            tags = sorted(nodes_rank.items(),key=itemgetter(1),reverse=True)
        else:
            tags = sorted(nodes_rank,key=nodes_rank.__getitem__,reverse=True)

        if topK:
            return  tags[:topK]
        else:
            return tags
f = open('test.txt',encoding='utf-8')
s = f.read()
ans = TextRank()
print(ans.textrank(s,topK=20,withWeight=True,allowPOS=('ns','v','vn','n'),withFlag=True))