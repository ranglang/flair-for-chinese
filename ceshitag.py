from flair.models import SequenceTagger
from flair.data import Sentence
tagger = SequenceTagger.load("zh-ner")
s = list("广州经济区")
print(s)
sentence = Sentence(" ".join(s))
print(sentence)
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence.to_tagged_string())