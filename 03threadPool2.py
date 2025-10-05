from concurrent.futures import ThreadPoolExecutor
import time

def something(name, game):
    print(f"Thread Started {name}")
    time.sleep(3)
    print(f"Thread Ended {game}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(something,1,1)
    executor.submit(something,2,2)
    executor.submit(something,3,3)

print("Main Ended")