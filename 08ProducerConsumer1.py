#Producer Consumer Problem only using Lock

import threading
import random
from concurrent.futures import ThreadPoolExecutor

class Pipeline():
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self,thread_name):  #Consumer
        print(f"{thread_name} acquring consumer_lock")
        self.consumer_lock.acquire()
        print(f"{thread_name} reading message {self.message}")
        message = self.message
        print(f"{thread_name} acquring producer_lock")
        self.producer_lock.release()
        return message
    
    def set_message(self,message,thread_name):  #Producer

        print(f"{thread_name} acquring producer_lock has {message}")
        self.producer_lock.acquire()
        print(f"{thread_name} setting message {message}")
        self.message = message
        print(f"{thread_name} release consumer_lock")
        self.consumer_lock.release()

def producer(pipeline:Pipeline):
    for i in range(10):
        message = random.randint(1,101)
        pipeline.set_message(message,"Producer")

def consumer(pipeline:Pipeline):
    for i in range(10):
        pipeline.get_message("Consumer")

if __name__ == "__main__":

    pipeline = Pipeline()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer,pipeline)
        executor.submit(consumer,pipeline)

    print("Main Thread Ended")

