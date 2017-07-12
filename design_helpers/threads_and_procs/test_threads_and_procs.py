from threading import Thread
import threading
from multiprocessing import Process
import multiprocessing as mp
from time import sleep

t_event = threading.Event()
p_event = mp.Event()

t_flag = False

def proc_func(N,id):
	
	N=N/2

	for i in range(N):
		print 'Proc-%s: %s'%(id,i)
	sleep(2)

def thread_func(N, id):

	global t_flag

	N = N/2

	while not t_event.is_set():
		
		print 'Thread %s N: %s' %(id,N)
		print 'Starting proc'

		#p = Process(target=proc_func, name='proc-1', args=(N,1))
		#p.start()
		#print 'Thread %s sleeping'%id
		#sleep(5)

		#p.join()

		print 'Thread %s N: %s' %(id,N)

		t_flag = True

if __name__ == '__main__':

	N=10

	print 'Main proc N: ',N

	t = Thread(target=thread_func, name='thread-1', args=(N, 1))
	t.start()

	while not t_flag:
		pass

	t_event.set()
	t.join()

	print 'Thread %s killed' %t.name
	print 'Main proc N: ',N