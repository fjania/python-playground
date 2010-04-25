import random

def create_int_gauss(samples, mu, sigma, sigma_bound=None):
	#return [random.choice([2,4,7,9])*10 for x in range(transactions)]
	#return [random.choice([1,3])*30 for x in range(transactions)]
	#return [abs(int(random.gauss(60,10))) for x in range(transactions)]
	l =[int(random.gauss(mu,sigma)) for x in range(samples)]
	if sigma_bound:
		return [x for x in l if (x > mu - sigma_bound*sigma) and (x < mu + sigma_bound*sigma)]
	else:
		return l

def create_int_uniform(samples, upper, lower):
	return [random.randint(upper,lower) for x in range(samples)]

