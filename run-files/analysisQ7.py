import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
import datetime

# Import the three change making algorithms
sys.path.insert(0, "../divide-conquer/")
sys.path.insert(0, "../dynamic-programming")
sys.path.insert(0, "../greedy")

from changeslow import changeslow
from changegreedy import changegreedy
from changedp import changedp

### QUESTION 7 ###
def Q7(slow):

	lenV = []
	runtimeGreedy = []
	runtimeDP = []
	runtimeSlow = []

	numExp = 10
	maxRange = 1000
	if (slow):
		maxRange = 10 # some much smaller number

	for i in range(1, maxRange): # V can be of length 1 to (maxRange - 1)
		print "\n------ running V length=" + str(i) + "------"
		lenV.append(i)
		#print "lenV:", lenV
		runtimeGreedy.append(0)
		runtimeDP.append(0)
		runtimeSlow.append(0)

		for j in range(numExp): # run numExp experiments for this length of V
			print "\n  ---- running experiment=" + str(j + 1) + " ----"
			coinArray = []

			for k in range(i): # generate V of size i [1, rand, ..., rand, max=1 + 5*(maxRange-2)]
				if (k == 0):
					coinArray.append(1)
				else:
					randFrom = coinArray[len(coinArray) - 1] + 1
					randTo = coinArray[len(coinArray) - 1] + 5
					coinArray.append(random.randint(randFrom, randTo))
			change = random.randint(1, 30)
			#print "  coinArray:", coinArray				
			#print "  change:", change			

			print "  running greedy..."
			start = datetime.datetime.now()
			_, _ = changegreedy(coinArray, change)
			end = datetime.datetime.now()
			delta = end - start
			delta = int(delta.total_seconds() * 1000000)
			print "    " + str(delta)
			runtimeGreedy[i - 1] += delta

			print "  running DP..."
			start = datetime.datetime.now()
			_, _ = changedp(coinArray, change)
			end = datetime.datetime.now()
			delta = end - start
			delta = int(delta.total_seconds() * 1000000)
			print "    " + str(delta)
			runtimeDP[i - 1] += delta
			
			if (slow):
				print "  running slow..."
				start = datetime.datetime.now()
				_, _ = changeslow(coinArray, change)
				end = datetime.datetime.now()
				delta = end - start
				delta = int(delta.total_seconds() * 1000000)
				print "    " + str(delta)
				runtimeSlow[i - 1] += delta

		runtimeGreedy[i - 1] /= numExp 
		runtimeDP[i - 1] /= numExp
		if (slow):
			runtimeSlow[i - 1] /= numExp

	plt.figure(21)
	plt.plot(lenV, runtimeGreedy, 'b-', linewidth=2.0, label='Greedy')
	plt.plot(lenV, runtimeDP, 'r--', linewidth=2.0, label='DP')
	if (slow):
		plt.plot(lenV, runtimeSlow, 'g-.', linewidth=2.0, label='Slow')
	plt.legend(loc='upper left')
	plt.title('Runtime vs len(V[]) for randomized V[] and A')
	plt.ylabel('Avg. Runtime (10^-6 sec)')
	plt.xlabel('len(V[])')
	plt.grid(True)
	if (slow):
		plt.savefig('img/Q7slow_runtime.png', bbox_inches='tight')
	else:
		plt.savefig('img/Q7_runtime.png', bbox_inches='tight')
		

def main():
	Q7(False)
	#Q7(True)


if __name__ == "__main__":
	main()
