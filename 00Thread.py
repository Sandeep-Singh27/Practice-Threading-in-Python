import threading
import time

def something(name):
    print(f"Thread {name} Starting")
    time.sleep(3)
    print(f"Thread {name} Ended")

Thread1 = threading.Thread(target=something,args=(1,))
Thread2 = threading.Thread(target=something,args=(2,))
Thread3 = threading.Thread(target=something,args=(3,))

Thread1.start()
Thread2.start()
Thread3.start()

print("Main Ended")
