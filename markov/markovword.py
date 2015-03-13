from collections import defaultdict
import random
import string

past = 4

allwords = []
words = []
with open('words-en.txt') as fp:
    for line in fp.readlines():
        allwords.append(line.strip())
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

real_words = []
fake_words = []

def run_test(count):
    for i in range(count):
        w = generate_word()
        if not w is None:
            is_word = w in allwords
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
    word_list_to_show.extend(real_words[0:real_words_to_show])
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

run_test(1000)
show_word_board()
show_word_board()
show_word_board()
show_word_board()
show_word_board()
