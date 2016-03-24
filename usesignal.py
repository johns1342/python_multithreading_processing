import signal
import time

shutdown = False

def sighandler(signum, frame):
	global shutdown
	print("Detected a shutdown request with signal {}".format(signum))
	shutdown = True

signal.signal(signal.SIGTERM, sighandler)
signal.signal(signal.SIGINT, sighandler)
signal.signal(signal.SIGHUP, sighandler)

while not shutdown:
	time.sleep(0.1)
