import random

count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for _ in range (0,100000):
	a = int(str(random.randint(1,9))[0:1])
	count[a-1] += 1
	
print count