from collections import defaultdict
import pprint

words = open("../dictionaries/us-english.txt", 'r')

anagrams = defaultdict(lambda : [])
histogram = defaultdict(lambda : defaultdict(lambda : 0))
min_word_len = 100
max_word_len = 0
total_words = 0

for word in words.readlines():
	word = word.rstrip()

	if len(word) < min_word_len:
		min_word_len = len(word)
	elif len(word) > max_word_len:
		max_word_len = len(word)

	sword = ''.join(sorted(word))
	anagrams[sword] += [word]
	total_words += 1

for sword in anagrams:
	histogram[len(sword)][len(anagrams[sword])] += 1

for key in histogram:
	print "%2s" % key,
	for count in histogram[key]:
		print "%5s : %5s" % (count, histogram[key][count]),
	print '\n'
# print histogram

print "Total number of words in dictionary: %s" % total_words
print "Maximum word length: %s" % max_word_len
print "Minimum word length: %s" % min_word_len