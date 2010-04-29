def memoize(f):
	memoized = {}
	def wrapped(arg):
		if memoized.get(arg):
			print "cache hit:", arg
			return memoized.get(arg)
		else:
			print "cache MISS:" , arg
			memoized[arg] = f(arg)
			return f(arg)
	return wrapped
	

@memoize
def do_something(text):
	# print text
	return text

do_something("hello")
do_something("hello")
do_something("hello")
do_something("nothing")
do_something("hello")

@memoize
def fibonacci_memoized(n):
  if n in (0, 1): return n
  return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

print "f(10):" , fibonacci_memoized(10)


def dfwa(a1, a2):
	def wrap(f):
		print "< in wrap" , a1
		f()
		print "> out of wrap" , a2
	return wrap

@dfwa('one', 'two')
def test_it():
	print "in test_it"
