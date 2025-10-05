# daemon are the process running in background
# daemon thread are the threads that get terminated when the program ended
# when code is executed if the threads are non-daemonic then programmic 

import threading
import time

def something(name):
    print(f"Thread {name} Starting")
    time.sleep(3)
    print(f"Thread {name} Ended")

Thread1 = threading.Thread(target=something,args=(1,), daemon=True)
Thread2 = threading.Thread(target=something,args=(2,), daemon=True)
Thread3 = threading.Thread(target=something,args=(3,), daemon=True)

Thread1.start()
Thread2.start()
Thread3.start()

print("Main Ended")
