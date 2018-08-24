from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import os
from Tools import *
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        catelist = os.listdir(self.dirname)
        print(self.dirname)
        for mydir in catelist:
            class_path = self.dirname + mydir + "/"
            file_list = os.listdir(class_path)
            for file_path in file_list:
                fullname = class_path + file_path
                content = readfile(fullname)
                try:
                    content = content.decode('UTF-8')
                except:
                    content = content.decode('gbk')
                content =content.replace(" ","")
                yield list(content)

class MySentences2(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        catelist = os.listdir(self.dirname)
        print (self.dirname)
        for mydir in catelist:
            class_path = self.dirname + mydir + "/"
            file_list = os.listdir(class_path)
            for file_path in file_list:
                fullname = class_path + file_path
                content = readfile(fullname)
                try:
                    content = content.decode('UTF-8')
                except:
                    content = content.decode('gbk')
                yield content.split()


sentences = MySentences("E:/训练集分词/")  # a memory-friendly iterator
model = Word2Vec(sentences,iter=10,workers=16,min_count=3,size=100,window=4,alpha=0.025, min_alpha=0.025)
model.save('./train.bin')








