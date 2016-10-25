'''
Program:                projectTwo.py
Authors:                Kyle Guthrie, Alex Miranda, Cash Stramel
Class/Section:          CS325-400
Due Date:               October 2016
Program Description:    Given a problem set, this program generates solutions
                        from three different "coin change" algorithms. Coded in 
                        Python and designed to run on Oregon State University's 
                        'flip' servers.
'''
import sys
import os

# Import the three change making algorithms
sys.path.insert(0, "../divide-conquer/")
sys.path.insert(0, "../dynamic-programming")
sys.path.insert(0, "../greedy")

from changeslow import changeslow
from changegreedy import changegreedy
from changedp import changedp

# Grab input file name with extension removed
# http://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python
inputFileName = sys.argv[1]
inputFileBase = os.path.splitext(inputFileName)[0]

# Define output file name based on project specifications
outputFileName = inputFileBase + "change.txt"


'''
Parse the input file

Expected input structure:
    - First line contains an array of coin denominations in increasing order
    - Second line contains one integer value for which we must make change

    Each pair of lines represents one problem
'''
coinArray = []
change = []
with open(inputFileName) as inputFile:
	for i, line in enumerate(inputFile):
		line = line.rstrip('\r\n')
		if line:
			# Odd lines define the coin array
			if (i + 1) % 2:
				arrayString = line.replace('[','').replace(']','').split(',')
				coinArray.append([int(i) for i in arrayString])
			# Even lines define the amount of change to make
			else:
				change.append(int(line))


'''
Generate the results file

For each of the three algorithms, run the provided problems through and write 
the results into the output file.
'''

# If output file already exists, remove it
# http://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
try:
	os.remove(outputFileName)
except OSError:
	pass

outputFile = open(outputFileName, 'w')

algorithmHeader = {0: "Algorithm changeslow:\n",
				1: "Algorithm changegreedy:\n",
				2: "Algorithm changedp:\n"};

# Run all of the provided problems through each of the three change algorithms
for algorithm in range(3):
	
	# Separate each results section with a header noting the algorithm used
	outputFile.write(algorithmHeader[algorithm])

	for i, _ in enumerate(coinArray):
		if algorithm == 0:
			coinCount, totalCoins = changeslow(coinArray[i], change[i])
		elif algorithm == 1:
			coinCount, totalCoins = changegreedy(coinArray[i], change[i])
		elif algorithm == 2:
			coinCount, totalCoins = changedp(coinArray[i], change[i])

		# Write the solutions from the given algorithm to the output file
		outputFile.write(str(coinCount) + '\n')
		outputFile.write(str(totalCoins) + '\n')

	outputFile.write('\n\n')

outputFile.close()