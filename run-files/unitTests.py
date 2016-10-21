'''
Program:                unitTests.py
Authors:                Kyle Guthrie, Alex Miranda, Cash Stramel
Class/Section:          CS325-400
Due Date:               October 2016
Program Description:    Unit tests for the three change making algorithms 
                        implemented for Project 2.
'''
import sys
import os
import unittest

# Import the three change making algorithms
sys.path.insert(0, "../divide-conquer/")
sys.path.insert(0, "../dynamic-programming")
sys.path.insert(0, "../greedy")

from changeslow import changeslow
from changegreedy import changegreedy
from changedp import changedp


### TEST CASES FOR THE 'changeslow' ALGORITHM ###
'''
class TestChangeSlow(unittest.TestCase):
	def test_trivial(self):
		coinCount, totalCoins = changeslow([1], 0)
		self.assertEqual(coinCount, [0])
		self.assertEqual(totalCoins, 0)

	def test_singleton(self):
		coinCount, totalCoins = changeslow([1], 1)
		self.assertEqual(coinCount, [1])
		self.assertEqual(totalCoins, 1)

	def test_powers_of_two(self):
		coinCount, totalCoins = changeslow([1, 2, 4, 8], 15)
		self.assertEqual(coinCount, [1, 1, 1, 1])
		self.assertEqual(totalCoins, 4)

	def test_suboptimal(self):
		coinCount, totalCoins = changeslow([1, 3, 7, 12], 29)
		self.assertEqual(coinCount, [0, 1, 2, 1])
		self.assertEqual(totalCoins, 4)

	def test_optimal(self):
		coinCount, totalCoins = changeslow([1, 3, 7, 12], 31)
		self.assertEqual(coinCount, [0, 0, 1, 2])
		self.assertEqual(totalCoins, 3)
'''

### TEST CASES FOR THE 'changegreedy' ALGORITHM ###
class TestChangeGreedy(unittest.TestCase):
	def test_trivial(self):
		coinCount, totalCoins = changegreedy([1], 0)
		self.assertEqual(coinCount, [0])
		self.assertEqual(totalCoins, 0)

	def test_singleton(self):
		coinCount, totalCoins = changegreedy([1], 1)
		self.assertEqual(coinCount, [1])
		self.assertEqual(totalCoins, 1)

	def test_powers_of_two(self):
		coinCount, totalCoins = changegreedy([1, 2, 4, 8], 15)
		self.assertEqual(coinCount, [1, 1, 1, 1])
		self.assertEqual(totalCoins, 4)

	def test_suboptimal(self):
		coinCount, totalCoins = changegreedy([1, 3, 7, 12], 29)
		self.assertEqual(coinCount, [2, 1, 0, 2])
		self.assertEqual(totalCoins, 5)

	def test_optimal(self):
		coinCount, totalCoins = changegreedy([1, 3, 7, 12], 31)
		self.assertEqual(coinCount, [0, 0, 1, 2])
		self.assertEqual(totalCoins, 3)

### TEST CASES FOR THE 'changedp' ALGORITHM ###
class TestChangeDP(unittest.TestCase):
	def test_trivial(self):
		coinCount, totalCoins = changedp([1], 0)
		self.assertEqual(coinCount, [0])
		self.assertEqual(totalCoins, 0)

	def test_singleton(self):
		coinCount, totalCoins = changedp([1], 1)
		self.assertEqual(coinCount, [1])
		self.assertEqual(totalCoins, 1)

	def test_powers_of_two(self):
		coinCount, totalCoins = changedp([1, 2, 4, 8], 15)
		self.assertEqual(coinCount, [1, 1, 1, 1])
		self.assertEqual(totalCoins, 4)

	def test_suboptimal(self):
		coinCount, totalCoins = changedp([1, 3, 7, 12], 29)
		self.assertEqual(coinCount, [0, 1, 2, 1])
		self.assertEqual(totalCoins, 4)

	def test_optimal(self):
		coinCount, totalCoins = changedp([1, 3, 7, 12], 31)
		self.assertEqual(coinCount, [0, 0, 1, 2])
		self.assertEqual(totalCoins, 3)

if __name__ == '__main__':
	unittest.main()