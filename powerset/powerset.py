def powerset(s):
	for i in range(2**len(s)):
		yield "".join([x for a, x in enumerate(s) if (1 << a) & i])

if __name__ == "__main__":
	import sys
	for x in powerset(sys.argv[1]):
		print x