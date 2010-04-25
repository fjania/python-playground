import sys
available_coins = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]

def make_change(amount):
	coins = []
	
	for coin in available_coins:
		while (amount - coin >= 0):
			coins.append(coin)
			amount -= coin
	
	print "Coins: ", coins
	
if __name__ == "__main__":
	make_change(int(sys.argv[1]))