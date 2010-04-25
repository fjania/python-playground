import random
import histogram
import distribution

def create_segment(transactions=50):
	#return [random.choice([2,4,7,9])*10 for x in range(transactions)]
	#return [random.choice([1,3])*30 for x in range(transactions)]
	#return [random.randint(20,99) for x in range(transactions)]
	#return [abs(int(random.gauss(60,10))) for x in range(transactions)]
	return distribution.create_int_gauss(transactions,60,15,4)

def do_random_observation(segment):
	time = random.randint(1, sum(segment)-1)
	count = 0
	for x in segment:
		count += x
		if count >= time : return x	

def do_many_observations(observations):
	total_time = 0
	total_transactions = 0

	observed_time = 0
	observed_transactions = 0

	for x in range(0,observations):
		segment = create_segment(abs(int(random.gauss(50,20)))+10)
		histogram.log_frequency(segment)	

		total_time += sum(segment)
		total_transactions += len(segment)

		observed = do_random_observation(segment)
		observed_time += observed

		avg_time_per_order = float(total_time) / total_transactions
		avg_time_observed = float(observed_time) / (x+1)


	return ( observations, total_transactions, avg_time_per_order, avg_time_observed, avg_time_observed - avg_time_per_order)
	
def do_many_trials(trials):
	total_delta = 0
	output = ""

	output +=  "+-------+--------------+--------------+---------+----------+---------+\n"
	output +=  "| Trial | Transactions | Observations | Average | Observed |  Delta  |\n" 
	output +=  "+-------+--------------+--------------+---------+----------+---------+\n"

	for trial in range(1, trials+1):
		observations, total_transactions, avg_time_per_order, avg_time_observed, delta = do_many_observations(random.randint(20,100))
		total_delta += delta

		output += "| %5d | %-12d | %-12d | %-7.2f | %-8.2f | %-7.2f |\n" % (
			trial,
			total_transactions, 
			observations, 
			avg_time_per_order,
			avg_time_observed,
			delta,
		)


	avg_delta = float(total_delta) / trials

	output +=  "+-------+--------------+--------------+---------+----------+---------+\n"
	output +=  "|                                                  Average | %-7.2f |\n" % (avg_delta)
	output +=  "+----------------------------------------------------------+---------+"

	return output


table = do_many_trials(50)
histogram = histogram.create_histogram("Distribution of Transaction Times", 31)

l_table = table.split('\n')
l_histogram = histogram.split('\n')

if len(l_table) > len(l_histogram):
	l_histogram += ['']*(len(l_table) - len(l_histogram))

elif len(l_histogram) > len(l_table):
	l_table += ["                                                                      "] * (len(l_histogram) - len(l_table))

z = zip(l_table, l_histogram)
print "\n".join([x + "   " + y for x,y in z])
