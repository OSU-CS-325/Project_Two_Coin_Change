import sys
import matplotlib.pyplot as plt

# Import the three change making algorithms
sys.path.insert(0, "../divide-conquer/")
sys.path.insert(0, "../dynamic-programming")
sys.path.insert(0, "../greedy")

from changeslow import changeslow
from changegreedy import changegreedy
from changedp import changedp

### QUESTION 3 ###
coinArray = [1, 5, 10, 25, 50]
change = range(2010, 2201)

numCoinsGreedy = [0] * len(change)
numCoinsDP = [0] * len(change)

for i, amt in enumerate(change):
	_, numCoinsGreedy[i] = changegreedy(coinArray, amt)
	_, numCoinsDP[i] = changedp(coinArray, amt)

plt.figure(1)
plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0, label='Greedy')
plt.plot(change, numCoinsDP, 'r--', linewidth=2.0, label='DP')
plt.legend(loc='upper left')
plt.ylabel('# of Coins')
plt.xlabel('Change Amount')
plt.grid(True)
plt.savefig('Q3.png', bbox_inches='tight')


### QUESTION 4 ###
coinArray1 = [1, 2, 6, 12, 24, 48, 60] 
coinArray2 = [1, 6, 13, 37, 150]
change = range(2000, 2201)

numCoinsGreedy1 = [0] * len(change)
numCoinsGreedy2 = [0] * len(change)
numCoinsDP1 = [0] * len(change)
numCoinsDP2 = [0] * len(change)

for i, amt in enumerate(change):
	_, numCoinsGreedy1[i] = changegreedy(coinArray1, amt)
	_, numCoinsGreedy2[i] = changegreedy(coinArray2, amt)
	_, numCoinsDP1[i] = changedp(coinArray1, amt)
	_, numCoinsDP2[i] = changedp(coinArray2, amt)

plt.figure(2)
plt.plot(change, numCoinsGreedy1, 'b-', linewidth=2.0, label='Greedy')
plt.plot(change, numCoinsDP1, 'r--', linewidth=2.0, label='DP')
plt.legend(loc='upper left')
plt.ylabel('# of Coins')
plt.xlabel('Change Amount')
plt.grid(True)
plt.savefig('Q4a.png', bbox_inches='tight')

plt.figure(3)
plt.plot(change, numCoinsGreedy2, 'b-', linewidth=2.0, label='Greedy')
plt.plot(change, numCoinsDP2, 'r--', linewidth=2.0, label='DP')
plt.legend(loc='upper left')
plt.ylabel('# of Coins')
plt.xlabel('Change Amount')
plt.grid(True)
plt.savefig('Q4b.png', bbox_inches='tight')

### QUESTION 5 ###
coinArray = [1] + range(2, 31, 2)
change = range(2000, 2201)

numCoinsGreedy = [0] * len(change)
numCoinsDP = [0] * len(change)

for i, amt in enumerate(change):
	_, numCoinsGreedy[i] = changegreedy(coinArray, amt)
	_, numCoinsDP[i] = changedp(coinArray, amt)

plt.figure(4)
plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0, label='Greedy')
plt.plot(change, numCoinsDP, 'r--', linewidth=2.0, label='DP')
plt.legend(loc='upper left')
plt.ylabel('# of Coins')
plt.xlabel('Change Amount')
plt.grid(True)
plt.savefig('Q5.png', bbox_inches='tight')