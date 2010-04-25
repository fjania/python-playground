import random
import math

d = {}
bucket_size = 5

def log_frequency(distribution):
	for z in distribution:
		d[bucket_size*int(z/bucket_size)] = d.get(bucket_size*int(z/bucket_size), 0) + 1


def create_histogram(title, max_height=50):
	_title = " " + title + " "
	output = ""
	output += "=" * 4 + _title + "=" * 4 + "\n"
	output += "\n"
	max_value = int(max(d.values()))
	for a in range(min(sorted(d)), max(sorted(d))+bucket_size, bucket_size):

		if bucket_size > 1 :
			bucket_label = "%4d-%-4d: " % (a, a+(bucket_size-1))
		elif bucket_size == 1 :
			bucket_label = "%4d: " % (a)
		else:
			raise Exception

		val = (float(d.get(a,0)) * max_height / max_value)

		if val == 0 :
			output += bucket_label + "\n"
		elif val < 1 :
			#print bucket_label + "." + " (%d)" % (d.get(a,0))
			output += bucket_label + "." + "\n"
		else :
			#print bucket_label + ( "-" * int(math.floor(val)) ) + " (%d)" % (d.get(a,0))
			output += bucket_label + ( "-" * int(math.floor(val)) ) + "\n"

	return output
