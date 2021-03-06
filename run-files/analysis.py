import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

# Import the three change making algorithms
sys.path.insert(0, "../divide-conquer/")
sys.path.insert(0, "../dynamic-programming")
sys.path.insert(0, "../greedy")

from changeslow import changeslow
from changegreedy import changegreedy
from changedp import changedp

### QUESTION 3 ###
def Q3():
	coinArray = [1, 5, 10, 25, 50]
	change = range(2010, 2201)

	numCoinsGreedy = [0] * len(change)
	numCoinsDP = [0] * len(change)

	runtimeGreedy = [0] * len(change)
	runtimeDP = [0] * len(change)

	for i, amt in enumerate(change):
		for j in range(10):
			t0 = time.clock()
			_, numCoinsGreedy[i] = changegreedy(coinArray, amt)
			runtimeGreedy[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP[i] = changedp(coinArray, amt)
			runtimeDP[i] += time.clock() - t0

		runtimeGreedy[i] /= 10
		runtimeDP[i] /= 10

	plt.figure(1)
	plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 5, 10, 25, 50]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q3.png', bbox_inches='tight')

	plt.figure(20)
	plt.plot(change, runtimeGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 5, 10, 25, 50]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q3_runtime.png', bbox_inches='tight')

### QUESTION 3 WITH SLOW ###
def Q3slow():
	coinArray = [1, 5, 10, 25, 50]
	change = range(1, 30)

	numCoinsGreedy = [0] * len(change)
	numCoinsDP = [0] * len(change)
	numCoinsSlow = [0] * len(change)

	runtimeGreedy = [0] * len(change)
	runtimeDP = [0] * len(change)
	runtimeSlow = [0] * len(change)

	for i, amt in enumerate(change):
		for j in range(10):
			t0 = time.clock()
			_, numCoinsGreedy[i] = changegreedy(coinArray, amt)
			runtimeGreedy[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP[i] = changedp(coinArray, amt)
			runtimeDP[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsSlow[i] = changeslow(coinArray, amt)
			runtimeSlow[i] += time.clock() - t0

		runtimeGreedy[i] /= 10
		runtimeDP[i] /= 10
		runtimeSlow[i] /= 10

	plt.figure(2)
	plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, numCoinsSlow, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 5, 10, 25, 50]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q3_slow.png', bbox_inches='tight')

	plt.figure(21)
	plt.plot(change, runtimeGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, runtimeSlow, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 5, 10, 25, 50]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q3slow_runtime.png', bbox_inches='tight')

### QUESTION 4 ###
def Q4():
	coinArray1 = [1, 2, 6, 12, 24, 48, 60] 
	coinArray2 = [1, 6, 13, 37, 150]
	change = range(2000, 2201)

	numCoinsGreedy1 = [0] * len(change)
	numCoinsGreedy2 = [0] * len(change)
	numCoinsDP1 = [0] * len(change)
	numCoinsDP2 = [0] * len(change)

	runtimeGreedy1 = [0] * len(change)
	runtimeGreedy2 = [0] * len(change)
	runtimeDP1 = [0] * len(change)
	runtimeDP2 = [0] * len(change)

	for i, amt in enumerate(change):
		for j in range(10):
			t0 = time.clock()
			_, numCoinsGreedy1[i] = changegreedy(coinArray1, amt)
			runtimeGreedy1[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsGreedy2[i] = changegreedy(coinArray2, amt)
			runtimeGreedy2[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP1[i] = changedp(coinArray1, amt)
			runtimeDP1[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP2[i] = changedp(coinArray2, amt)
			runtimeDP2[i] += time.clock() - t0

		runtimeGreedy1[i] /= 10
		runtimeGreedy2[i] /= 10
		runtimeDP1[i] /= 10
		runtimeDP2[i] /= 10

	plt.figure(3)
	plt.plot(change, numCoinsGreedy1, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP1, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 6, 12, 24, 48, 60]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4a.png', bbox_inches='tight')

	plt.figure(4)
	plt.plot(change, numCoinsGreedy2, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP2, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 6, 13, 37, 150]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4b.png', bbox_inches='tight')

	plt.figure(22)
	plt.plot(change, runtimeGreedy1, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP1, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 6, 12, 24, 48, 60]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4a_runtime.png', bbox_inches='tight')

	plt.figure(23)
	plt.plot(change, runtimeGreedy2, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP2, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 6, 13, 37, 150]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4b_runtime.png', bbox_inches='tight')

### QUESTION 4 WITH SLOW ###
def Q4slow():
	coinArray1 = [1, 2, 6, 12, 24, 48, 60] 
	coinArray2 = [1, 6, 13, 37, 150]
	change = range(1, 30)

	numCoinsGreedy1 = [0] * len(change)
	numCoinsGreedy2 = [0] * len(change)
	numCoinsSlow1 = [0] * len(change)
	numCoinsSlow2 = [0] * len(change)
	numCoinsDP1 = [0] * len(change)
	numCoinsDP2 = [0] * len(change)

	runtimeGreedy1 = [0] * len(change)
	runtimeGreedy2 = [0] * len(change)
	runtimeDP1 = [0] * len(change)
	runtimeDP2 = [0] * len(change)
	runtimeSlow1 = [0] * len(change)
	runtimeSlow2 = [0] * len(change) 

	for i, amt in enumerate(change):
		for j in range(10):
			t0 = time.clock()
			_, numCoinsGreedy1[i] = changegreedy(coinArray1, amt)
			runtimeGreedy1[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsGreedy2[i] = changegreedy(coinArray2, amt)
			runtimeGreedy2[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP1[i] = changedp(coinArray1, amt)
			runtimeDP1[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP2[i] = changedp(coinArray2, amt)
			runtimeDP2[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsSlow1[i] = changeslow(coinArray1, amt)
			runtimeSlow1[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsSlow2[i] = changeslow(coinArray2, amt)
			runtimeSlow2[i] += time.clock() - t0

		runtimeGreedy1[i] /= 10
		runtimeGreedy2[i] /= 10
		runtimeDP1[i] /= 10
		runtimeDP2[i] /= 10
		runtimeSlow1[i] /= 10
		runtimeSlow2[i] /= 10
			

	plt.figure(5)
	plt.plot(change, numCoinsGreedy1, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP1, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, numCoinsSlow1, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 6, 12, 24, 48, 60]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4a_slow.png', bbox_inches='tight')

	plt.figure(6)
	plt.plot(change, numCoinsGreedy2, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP2, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, numCoinsSlow2, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 6, 13, 37, 150]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4b_slow.png', bbox_inches='tight')

	plt.figure(24)
	plt.plot(change, runtimeGreedy1, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP1, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, runtimeSlow1, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 6, 12, 24, 48, 60]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4aslow_runtime.png', bbox_inches='tight')

	plt.figure(25)
	plt.plot(change, runtimeGreedy2, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP2, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, runtimeSlow2, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 6, 13, 37, 150]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q4bslow_runtime.png', bbox_inches='tight')

### QUESTION 5 ###
def Q5():
	coinArray = [1] + range(2, 31, 2)
	change = range(2000, 2201)

	numCoinsGreedy = [0] * len(change)
	numCoinsDP = [0] * len(change)

	runtimeGreedy = [0] * len(change)
	runtimeDP = [0] * len(change)

	for i, amt in enumerate(change):
		for j in range(10):
			t0 = time.clock()
			_, numCoinsGreedy[i] = changegreedy(coinArray, amt)
			runtimeGreedy[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP[i] = changedp(coinArray, amt)
			runtimeDP[i] += time.clock() - t0

		runtimeGreedy[i] /= 10
		runtimeDP[i] /= 10


	plt.figure(7)
	plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 4, 6, ..., 28, 30]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q5.png', bbox_inches='tight')

	plt.figure(26)
	plt.plot(change, runtimeGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP, 'r--', linewidth=2.0, label='DP')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 4, 6, ..., 28, 30]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q5_runtime.png', bbox_inches='tight')

### QUESTION 5 WITH SLOW ###
def Q5slow():
	coinArray = [1] + range(2, 31, 2)
	change = range(1, 30)

	numCoinsGreedy = [0] * len(change)
	numCoinsDP = [0] * len(change)
	numCoinsSlow = [0] * len(change)

	runtimeGreedy = [0] * len(change)
	runtimeDP = [0] * len(change)
	runtimeSlow = [0] * len(change)

	for i, amt in enumerate(change):
		for j in range(10):
			t0 = time.clock()
			_, numCoinsGreedy[i] = changegreedy(coinArray, amt)
			runtimeGreedy[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsDP[i] = changedp(coinArray, amt)
			runtimeDP[i] += time.clock() - t0

			t0 = time.clock()
			_, numCoinsSlow[i] = changeslow(coinArray, amt)
			runtimeSlow[i] += time.clock() - t0

		runtimeGreedy[i] /= 10
		runtimeDP[i] /= 10
		runtimeSlow[i] /= 10

	plt.figure(8)
	plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, numCoinsDP, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, numCoinsSlow, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 4, 6, ..., 28, 30]')
	plt.ylabel('# of Coins')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q5_slow.png', bbox_inches='tight')

	plt.figure(27)
	plt.plot(change, runtimeGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(change, runtimeDP, 'r--', linewidth=2.0, label='DP')
	plt.plot(change, runtimeSlow, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('V = [1, 2, 4, 6, ..., 28, 30]')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q5slow_runtime.png', bbox_inches='tight')


def main():
	Q3()
	Q3slow()
	Q4()
	Q4slow()
	Q5()
	Q5slow()


if __name__ == "__main__":
	main()