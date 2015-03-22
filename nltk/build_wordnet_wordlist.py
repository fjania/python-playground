import json
import math

from nltk.corpus import wordnet as wn

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

words = []
with open('../dictionaries/word_frequencies.txt') as fp:
    for w in fp.readlines():
        words.append(w.strip().split(' '))

output_words = []
for w in words:
    freq = w[0]
    word = w[1]

    if (not is_ascii(word)):
        continue

    ss = wn.synsets(word)
    if (len(ss) > 0):
        s = wn.synset(wn.synsets(word)[0].name())
        output = {
            "w": word,
            "f": freq,
            "d": s.definition(),
            "p": s.pos(),
        }
        output_words.append(output)

total = len(output_words)
for i, ow in enumerate(output_words):
    ow['s'] = math.floor(float(i+1.0)/total * 100)

print json.dumps(output_words, indent=2)
