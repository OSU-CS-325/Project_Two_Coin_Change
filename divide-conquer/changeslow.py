'''
Function:		changeslow
Description:	Implements a brute force (divide-and-conquer) solution to the 
				change making problem.
Receives:		coinArray - denominations of available coins
				change - amount to make change for
Returns:		coinCount - the number of each coin denomination used
				minCoins - the total number of coins used to make change

Preconditions:	change >= 0
				coinArray non-empty
'''
def changeslow(coinArray, change):
	# coinCount will store the number of each coin used
	coinCount = [0] * len(coinArray)

	# If change is one of the coins, we can exit early since it takes 1 coin
	if change in coinArray:
		coinCount[coinArray.index(change)] = 1
		return coinCount, 1
	# You can't make change for 0 with any coins
	elif change == 0:
		return coinCount, 0

	# Starting min at infinity guarantees some amount will be less
	minCoins = float('inf')

	# Divide the sums into left and right halves, searching for the minimum.
	# Note that looping past change/2 duplicates effort due to the symmetry of 
	# the function calls.
	for i in range(1, change/2 + 1):
		coinCountLeft, minCoinsLeft = changeslow(coinArray, i)
		coinCountRight, minCoinsRight = changeslow(coinArray, change - i)
		totalCoins = minCoinsLeft + minCoinsRight
		if totalCoins < minCoins:
			minCoins = totalCoins

			# Add the two lists of coins, element-wise
			# http://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
			coinCount = [x + y for x, y in zip(coinCountLeft, coinCountRight)]

	# Return the number of each coin used, and the overall number of coins
	return coinCount, minCoins