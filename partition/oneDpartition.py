import sys, math

length = sys.argv[1]

def partition(w, level):
	print "." * (level*3) + " " + str(w)
	if w > 1:
		l = w//2
		r = w - l
		(partition(l, level+1), partition(r, level+1))
	return w
	
partition(int(length), 0)