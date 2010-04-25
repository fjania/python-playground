wordlist = open('dict.txt').readlines()

def contains_word(dictword, testword):
	testletters = list(testword)
	for l in dictword:
		if not l in testletters:
			return None
		else:
			testletters.remove(l)
	return True

def anagram(word, min=3):
	anagrams = []
	for dictword in wordlist:
		dictword = dictword.rstrip()
		if len(dictword) <= word and len(dictword) >= min and contains_word(dictword, word):
				anagrams.append(dictword)
	return anagrams

if __name__ == "__main__":
	import sys
	print anagram(sys.argv[1])