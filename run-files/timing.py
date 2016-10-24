import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
from math import pow
import numpy as np
from scipy.optimize import curve_fit

# Import the three change making algorithms
sys.path.insert(0, "../divide-conquer/")
sys.path.insert(0, "../dynamic-programming")
sys.path.insert(0, "../greedy")

from changeslow import changeslow
from changegreedy import changegreedy
from changedp import changedp

fitOutput = open('fit_coefficients.txt', 'w')

def Q3():
	coinArray = [1, 5, 10, 25, 50]
	change = range(1000, 100001, 1000)
	# change = range(1000, 20001, 1000)
	change_small = range(1, 21, 1)

	runtimeGreedy = [0] * len(change)
	runtimeDP = [0] * len(change)
	runtimeSlow = [0] * len(change_small)

	for i, amt in enumerate(change):
		print("Q3 timing for change = " + str(amt))
		for j in range(10):
			t0 = time.clock()
			_, _ = changegreedy(coinArray, amt)
			runtimeGreedy[i] += time.clock() - t0

			t0 = time.clock()
			_, _ = changedp(coinArray, amt)
			runtimeDP[i] += time.clock() - t0

		runtimeGreedy[i] /= 10
		runtimeDP[i] /= 10

	for i, amt in enumerate(change_small):
		print("Q3_slow timing for change = " + str(amt))
		for j in range(10):
			t0 = time.clock()
			_, _ = changeslow(coinArray, amt)
			runtimeSlow[i] += time.clock() - t0

		runtimeSlow[i] /= 10

	# Create curve fits for each data set
	poptGreedy, pcovGreedy = curve_fit(linearCurve, np.asarray(change), np.asarray(runtimeGreedy))
	poptDP, pcovDP = curve_fit(linearCurve, np.asarray(change), np.asarray(runtimeDP))
	poptSlow, pcovSlow = curve_fit(exponentialCurve, np.asarray(change_small), np.asarray(runtimeSlow))

	fitOutput.write("Q3 Greedy Linear Curve Fit: \n")
	fitOutput.write("Slope = " + str(poptGreedy[0]) + "\n")
	fitOutput.write("Intercept = " + str(poptGreedy[1]) + "\n")
	fitOutput.write("\n\n")

	fitOutput.write("Q3 DP Linear Curve Fit: \n")
	fitOutput.write("Slope = " + str(poptDP[0]) + "\n")
	fitOutput.write("Intercept = " + str(poptDP[1]) + "\n")
	fitOutput.write("\n\n")

	fitOutput.write("Q3 Slow Exponential Curve Fit: \n")
	fitOutput.write("y = a*e^(b*x) + c \n")
	fitOutput.write("a = " + str(poptSlow[0]) + "\n")
	fitOutput.write("b = " + str(poptSlow[1]) + "\n")
	fitOutput.write("c = " + str(poptSlow[2]) + "\n")
	fitOutput.write("\n\n")

	fitGreedy = linearCurve(np.asarray(change), poptGreedy[0], poptGreedy[1])
	fitDP = linearCurve(np.asarray(change), poptDP[0], poptDP[1])
	fitSlow = exponentialCurve(np.asarray(change_small), poptSlow[0], poptSlow[1], poptSlow[2])

	plt.figure(1)
	plt.subplot(3, 1, 1)
	plt.plot(change, runtimeGreedy, 'k.', linewidth=2.0, label='Greedy data')
	plt.plot(change, fitGreedy, 'b--', linewidth=2.0, label='Curve Fit')
	plt.legend(loc='upper left')
	plt.ylabel('Avg. Runtime (sec)')
	plt.title('V = [1, 5, 10, 25, 50]')
	plt.grid(True)
	plt.subplot(3, 1, 2)
	plt.plot(change, runtimeDP, 'k.', linewidth=2.0, label='DP data')
	plt.plot(change, fitDP, 'r--', linewidth=2.0, label='Curve Fit')
	plt.legend(loc='upper left')
	plt.ylabel('Avg. Runtime (sec)')
	plt.grid(True)
	plt.subplot(3, 1, 3)
	plt.plot(change_small, runtimeSlow, 'k.', linewidth=2.0, label='Slow data')
	plt.plot(change_small, fitSlow, 'g--', linewidth=2.0, label='Curve Fit')
	plt.legend(loc='upper left')
	plt.ylabel('Avg. Runtime (sec)')
	plt.xlabel('Change Amount')
	plt.grid(True)
	plt.savefig('img/Q3_runtime_improved.png', bbox_inches='tight')


def Q4():
	coinArray1 = [1, 2, 6, 12, 24, 48, 60] 
	coinArray2 = [1, 6, 13, 37, 150]

	change = range(1000, 100001, 1000)

	runtimeGreedy1 = [0] * len(change)
	runtimeGreedy2 = [0] * len(change)
	runtimeDP1 = [0] * len(change)
	runtimeDP2 = [0] * len(change)


def main():
	Q3()


def linearCurve(x, m, b):
	return m*x + b

def exponentialCurve(x, a, b, c):
	return a * np.exp(b * x) + c

if __name__ == "__main__":
	main()