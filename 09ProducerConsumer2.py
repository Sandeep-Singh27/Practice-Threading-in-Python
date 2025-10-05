# Solution of Producer Consumer Problem using Queue

from threading import Event
from concurrent.futures import ThreadPoolExecutor
import time
from random import randint
from queue import Queue

#Pipeline class
class Pipeline():
    def __init__(self):
        self.message_queue = Queue(maxsize=10)
 
    def get_message(self,thread_name):
        message = self.message_queue.get()
        print(f"{thread_name} read message {message}")

    def set_message(self, thread_name, message):
        print(f"{thread_name} storing {message}")
        self.message_queue.put(message)

#Producer function
def producer(pipeline:Pipeline, event: Event):
    while not event.is_set():
        message = randint(1,101)
        pipeline.set_message("Producer",message)
    print("Event set, Producer Exiting...")

#Consumer function
def consumer(pipeline:Pipeline, event: Event):
    while not event.is_set() or pipeline.message_queue.empty():
        pipeline.get_message("Consumer")
    print("Event set, Consumer Exiting...")

#Driver's Code
if __name__ == "__main__":
    event = Event()
    pipeline = Pipeline()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer,pipeline, event)
        executor.submit(consumer,pipeline, event)

        time.sleep(0.01)
        print("MAIN: Setting the event")
        event.set()
