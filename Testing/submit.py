import requests, threading

def task(i):
    for c in range(10):
        resp = requests.post("http://localhost/44eee68d93bd9ce7c9eca0047bbdb460/add", data={'hund': (i//100)%10, 'ten': (i//10)%10, 'zero': i%10})
        #print (i)
        i += 1

for i in range(9, 50):
    start = i*10+1
    t = threading.Thread(target=task,args=(start,))
    t.start()
