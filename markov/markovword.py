from collections import defaultdict
import random
import string

past = 5

words = []
with open('words-en.txt') as fp:
    for line in fp.readlines():
        if len(line.strip()) > (1 + past):
            words.append(line.strip())


def tuples():
    for word in words:
        for i in range(len(word) - past):
            s = tuple([word[i + j] for j in range(past + 1)])
            yield s

cache = defaultdict(list)
for t in tuples():
    key = tuple(t[0:-1])
    value = t[-1]
    cache[key].append(value)

def generate_word():
    string_size = random.randint(past, past+4) - past

    seed = words[random.randint(0, len(words)-1)]
    s = tuple([seed[j] for j in range(past)])

    generated_word = []
    generated_word.extend(s)

    for i in range(string_size):
        next_letters = cache.get(s, [])

        if not next_letters:
            return None

        next_letter = random.choice(next_letters)
        generated_word.append(next_letter)
        a = []
        a.extend(s)
        a.append(next_letter)
        s = tuple(a[1:])

    return ''.join(generated_word)

def run_test(count):
    words_count = 0
    non_words_count = 0

    for i in range(count):
        w = generate_word()
        if not w is None:
            is_word = w in words
            if is_word:
                words_count +=1
            else:
                non_words_count += 1
            #print "{:<20s}{}".format(w, is_word)
            print w,

    print
    print "{:<20s}{}".format("Words", words_count)
    print "{:<20s}{}".format("Non-Words", non_words_count)

run_test(1000)
