import multiprocessing as mp
import Queue
import time

globalID = None
start = time.time()

# Function to call on every job
def jobThread(jobQueue, threadID):
	global globalID
	while True:
		try:
			job = jobQueue.get_nowait()
		except Queue.Empty:
			if jobQueue.empty(): break  # get_nowait() can timeout on a non-empty queue
		else:
			sleeptime = job
			now = time.time() - start
			print("{:.2f}: [{}] read globalID={}, setting to {}".format(
				now, threadID, globalID, threadID))
			globalID = threadID
			time.sleep(sleeptime)
			jobQueue.task_done()

# Function to start the processes
def doWork(jobs, maxworkers=10):
	jobCount = len(jobs)
	jobQueue = mp.JoinableQueue()
	for job in jobs:
		jobQueue.put(job)

	maxworkers = min(maxworkers, jobCount)

	processes = [mp.Process(target=jobThread, args=(jobQueue,n)) for n in range(maxworkers)]
	for p in processes:
		p.start()

	jobQueue.join()

# create job list
jobList = []
for i in xrange(20):
	jobList.append(1)

doWork(jobList)
print("{:.2f}: All done!".format(time.time() - start))
