import json

from nltk.corpus import wordnet as wn

words = []
with open('../dictionaries/words-en.txt') as fp:
    for w in fp.readlines():
        words.append(w.strip())

output_words = []
for w in words:
    ss = wn.synsets(w)
    if (len(ss) > 0):
        s = wn.synset(wn.synsets(w)[0].name())
        output = {
            "w": w,
            "d": s.definition(),
            "p": s.pos(),
        }
        output_words.append(output)

print json.dumps(output_words, indent=2)
