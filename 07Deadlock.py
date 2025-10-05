import threading

lock = threading.Lock()
print("Before Acquiring the lock")

lock.acquire()
print("After Acquiring the lock")

lock.acquire()
print("Acquiring the same lock twice")