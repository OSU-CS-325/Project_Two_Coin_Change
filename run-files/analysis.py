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

plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0)
plt.plot(change, numCoinsDP, 'r-', linewidth=2.0)
plt.ylabel('# of Coins')
plt.xlabel('Change Amount')
plt.show()