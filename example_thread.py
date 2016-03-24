import threading as tr
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
			break
		else:
			sleeptime = job
			now = time.time() - start
			print("{:.2f}: [{}] read globalID {}, setting to {}".format(
				now, threadID, globalID, threadID))
			globalID = threadID
			time.sleep(sleeptime)
			jobQueue.task_done()

# Function to start the threads
def doWork(jobs, maxworkers=10):
	jobCount = len(jobs)
	jobQueue = Queue.Queue()
	for job in jobs:
		jobQueue.put(job)

	maxworkers = min(maxworkers, jobCount)

	threads = [tr.Thread(target=jobThread, args=(jobQueue,n)) for n in range(maxworkers)]
	for t in threads:
		t.start()

	jobQueue.join()

# create job list
jobList = []
for i in xrange(20):
	jobList.append(1)

doWork(jobList)
print("{:.2f}: All done!".format(time.time() - start))
