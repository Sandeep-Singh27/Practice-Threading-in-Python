import threading

event = threading.Event()
i = 0
while not event.is_set():
    i += 1
    if i == 10: event.set()

print(i)
