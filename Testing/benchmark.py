import threading
import requests
import time

req_per_thread = 100
thread_count = 25

def task(name):
	for i in range(req_per_thread):
		resp = requests.get("http://localhost")
		#print ("Th: {0} - {1}".format(name, resp.text).strip())

t0 = time.time()
threads = []
for i in range(thread_count):
    t = threading.Thread(target=task,args=(i+1,))
    t.start()
    #t.join()

t.join()

t1 = time.time()
print ("REQUESTS: {0}".format(req_per_thread*thread_count))
print ("TIME 	: {0:.3f} sec".format(t1-t0))
print ("REQ/SEC : {0:.3f}".format(req_per_thread*thread_count/(t1-t0)))
