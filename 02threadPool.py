from concurrent.futures import ThreadPoolExecutor
import time

def something(i:tuple):
    name,game = i
    print(f"Thread {name} Starting")
    time.sleep(3)
    print(f"Thread  {game} Ended")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(something,[(1,11),(2,22),(3,33)])

print("Main Ended")
