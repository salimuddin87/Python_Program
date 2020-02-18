"""
Use two data structures to implement an LRU Cache.
	1. Queue -> which is implemented using a doubly linked list. The maximum
	   size of the queue will be equal to the total number of frames available
	   (cache size). The most recently used pages will be near front end and 
	   least recently pages will be near the rear end.
	2. Hash -> with page number as key and address of the corresponding queue node as value.

"""
import os
import sys

from queueOperations import Queue 

path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, path)


def LRU_cachePolicy(A, k):
	pass

if __name__ == "__main__":
	# cache hit is 8 for below example
	A = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
	pageSize = 3
	LRU_cachePolicy(A, k)