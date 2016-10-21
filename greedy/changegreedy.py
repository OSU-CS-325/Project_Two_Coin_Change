def changegreedy(coinArray, change):

	debug = False

	coinCount = [0 for x in range(len(coinArray))]
    
	if (debug):
		print "coinArray: ", coinArray
		print "change: ", change
		print "coinCount: ", coinCount, "\n"

	i = len(coinArray) - 1
	while (change > 0):

		if (change >= coinArray[i]):
			change -= coinArray[i]
			coinCount[i] += 1
			if (debug):
				print "change: ", change
				print "coinCount: ", coinCount, "\n"
                else:
			i -= 1 
	
	return coinCount, sum(coinCount)
