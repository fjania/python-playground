def memoize(f):
	memoized = {}
	def wrapped(arg):
		if memoized.get(arg):
			# print "cache hit  => memoized[%s]: %s" %(arg, memoized.get(arg))
			return memoized.get(arg)
		else:
			memoized[arg] = f(arg)
			print "cache MISS => memoized[%s]: %s" %(arg, memoized.get(arg))
			return f(arg)
	return wrapped
	

@memoize
def fibonacci_memoized(n):
  if n in (0, 1): return n
  return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

fibonacci_memoized(100)


def dfwa(a1, a2):
	def wrap(f):
		print "< in wrap" , a1
		f()
		print "> out of wrap" , a2
	return wrap

@dfwa('one', 'two')
def test_it():
	print "in test_it"
