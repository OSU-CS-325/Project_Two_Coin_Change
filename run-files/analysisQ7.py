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

### QUESTION 7 ###
def Q7():
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

### QUESTION 7 WITH SLOW ###
def Q7slow():
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

def main():
	Q7()
	Q7slow()


if __name__ == "__main__":
	main()
