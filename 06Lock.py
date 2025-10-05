import time
from concurrent.futures import ThreadPoolExecutor
import threading

class FakeDatebase():
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def update(self,index):
        self.lock.acquire()     #Acquiring the lock

        print(f"Thread {index} copying the value")
        local = self.value
        print(f"Thread {index} computation {local}")
        local += 1
        time.sleep(0.5)
        print(f"Thread {index} going to sleep ...")
        time.sleep(0.2)
        print(f"Thread {index} updating the value to {local}")
        self.value = local

        self.lock.release()     #Releasing the lock

database = FakeDatebase()

with ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(2):
        executor.submit(database.update,i)

print("Main Thread ended")
print(database.value)
