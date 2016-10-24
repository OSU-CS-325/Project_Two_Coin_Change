import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Import the DP and Greedy change making algorithms
sys.path.insert(0, "../dynamic-programming")
sys.path.insert(0, "../greedy")

from changegreedy import changegreedy
from changedp import changedp

def draw_plot(p, start, end):
  coinArray = [p**x for x in range(0, 4)]
  change = range(start, end)

  numCoinsGreedy = [0] * len(change)
  numCoinsDP = [0] * len(change)

  for i, amt in enumerate(change):
    _, numCoinsGreedy[i] = changegreedy(coinArray, amt)
    _, numCoinsDP[i] = changedp(coinArray, amt)

  plt.plot(change, numCoinsGreedy, 'b-', linewidth=2.0, label='Greedy')
  plt.plot(change, numCoinsDP, 'r--', linewidth=2.0, label='DP')
  plt.legend(loc='upper left')
  plt.ylabel('# of Coins')
  plt.xlabel('Change Amount')
  plt.grid(True)
  plt.savefig('img/%d.png' % (p))
  plt.clf()  

def main():
  draw_plot(3, 2000, 2201)
  draw_plot(4, 2000, 2201)
  draw_plot(5, 2000, 2201)

if __name__ == "__main__":
  main()
  
