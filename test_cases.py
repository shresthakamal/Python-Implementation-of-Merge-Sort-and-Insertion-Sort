

import unittest
import random
from insertion_sorting  import insertionSort
from merge_sorting import mergeSort

numberoftestcases=10000
class SearchTestCase(unittest.TestCase):
	# test for linear Search

	def test_insertionSort(self):
		
		randomnum=random.sample(range(100000),numberoftestcases)
		sortednum=sorted(randomnum)
		self.assertEqual(insertionSort(randomnum),sortednum) 

	def test_mergeSort(self):	
		randomnum=random.sample(range(100000),numberoftestcases)
		sortednum=sorted(randomnum)
		self.assertEqual(mergeSort(randomnum),sortednum) 


if __name__=='__main__':
	unittest.main()



