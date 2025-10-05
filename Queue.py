from queue import Queue
import random

a = Queue()
a.put("Text1")
a.put("Text2")
print(a.qsize())
print(a.get())
print(a.qsize())
print(a.get())
print(a.qsize())
b = a.get() if a.empty() == False else None
print(f"b is {b}")

c = Queue(maxsize=3)
while True:
    c.put(random.randint(1,10))
print("End of program")