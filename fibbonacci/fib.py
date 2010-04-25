import sys

def fib(end):

	a = 1
	b = 1
	for i in xrange(3, end+1):
		_a = a
		a = b
		b = _a + b
	
		yield b

if __name__ == '__main__':
	end = int(sys.argv[1])
	for i in fib(end):
		print i , ", ", 
