import threading as tr
import time

globalDict = {}  # Be very careful with global mutable objects
globalDictLock = tr.RLock() # Just use RLock, don't deadlock yourself
shutdown = False

def taskThread1(taskparams):
	while not shutdown:
		# ... do task ...
		state = 'state1'
		with globalDictLock:
			globalDict['task1'] = state
		time.sleep(0.1)


def taskThread2(taskparams):
	while not shutdown:
		# ... do task ...
		state = 'state2'
		with globalDictLock:
			globalDict['task2'] = state
		time.sleep(0.1)
