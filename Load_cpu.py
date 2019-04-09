#!/usr/bin/python3

'''
This python program runs a fictional load on desired number of threads on the PC, useful for PC examination under load.
Run as './Load_cpu.py', after chmod set to u+x.
'''

from argparse import ArgumentParser
from multiprocessing import Process
from signal import signal, SIGINT

shutdown = False

def signal_handler(sig, frame):
	global shutdown
	shutdown = True

def fibonacci(num):
	n1 = 0
	n2 = 1
	count = 0
	while count < num:
		nth = n1 + n2
		n1 = n2
		n2 = nth
		if shutdown:
			count = num
		else:
			count += 1
	return nth

if __name__ == '__main__':
	
	signal(SIGINT, signal_handler)
	print("Press 'Ctrl+C' to exit\n")
	
	parser = ArgumentParser(description="CPU dummy load")
	parser.add_argument("--thread", required=False, type=int, default=4, help="number of threads to load")
	args = parser.parse_args()
	
	jobs = []
	for i in [99999999]*args.thread:
		p = Process(target=fibonacci, args=(i,))
		jobs.append(p)
		p.start()
