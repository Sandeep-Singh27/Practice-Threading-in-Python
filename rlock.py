import threading

lock = threading.RLock()

lock.acquire()
lock.acquire()
print("Hello World")
lock.release()
lock.release()