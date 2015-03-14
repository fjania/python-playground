from collections import defaultdict
import json
import random
import string

past = 5

allwords = []
with open('../dictionaries/wordnet-words-en-defined.json') as fp:
    all_words = json.load(fp)

words = {}
word_set = set()
def tuples():
    for entry in all_words:
        word = entry.get('w')
        if len(word) > past:
            words[word] = entry
            word_set.add(word)
            for i in range(len(word) - past):
                s = word[i:i+past + 1]
                yield s

cache = defaultdict(list)
for t in tuples():
    key = t[0:-1]
    value = t[-1]
    if len(key) < past:
        print key, value
    cache[key].append(value)

def generate_word():
    string_size = random.randint(past, past+4) - past
    string_size = 2

    seed = random.sample(word_set,1)[0]
    s = seed[0:past]

    generated_word = s
    for i in range(string_size):
        next_letters = cache.get(s, [])

        if not next_letters:
            return None

        next_letter = random.choice(next_letters)
        generated_word += next_letter
        s = s[1:] + next_letter

    return generated_word

real_words = []
fake_words = []

def run_test(count):
    for i in range(count):
        w = generate_word()
        if not w is None:
            is_word = w in word_set
            if is_word:
                #real_words.append("[{}]".format(w))
                real_words.append("{}".format(w))
            else:
                fake_words.append(w)

    print "After {} attempts to generate words ({} successful)".format(
        count,
        len(real_words)+len(fake_words)
    )
    print "{:<20s}{}".format("Words", len(real_words))
    print "{:<20s}{}".format("Non-Words", len(fake_words))

def show_word_board():
    words_to_show = 36
    real_words_to_show = int(words_to_show * (len(real_words) / 1000.0))
    fake_words_to_show = words_to_show - real_words_to_show

    random.shuffle(real_words)
    random.shuffle(fake_words)
    word_list_to_show = []
    real_word_list_to_show = real_words[0:real_words_to_show]
    word_list_to_show.extend(real_word_list_to_show)
    word_list_to_show.extend(fake_words[0:fake_words_to_show])

    random.shuffle(word_list_to_show)
    print
    print "|--/ {} real words, {} fake words /----------------------------------------------|".format(
        real_words_to_show,
        fake_words_to_show
    )
    print "|                                                                               |"
    for x in range(6):
        print "| {:^12s} {:^12s} {:^12s} {:^12s} {:^12s} {:^12s} |".format(*word_list_to_show[x*6:x*6+6])

    print "|                                                                               |"
    print "|-------------------------------------------------------------------------------|"
    
    for w in real_word_list_to_show:
        entry = words[w]
        print "[{}] ({}) - {}".format(entry.get('w'), entry.get('p'), entry.get('d'))

run_test(1200)
show_word_board()
show_word_board()
show_word_board()
show_word_board()
show_word_board()
