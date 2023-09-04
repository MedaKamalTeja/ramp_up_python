import queue
import threading
#import sys

def producer(q, producer_id, num_items):
    for i in range(num_items):
        item = f"Item {producer_id}-{i}"
        q.put(item)
        print(f"Produced: {item}")

def consumer(q, consumer_id, num_items):
    for _ in range(num_items):
        item = q.get()
        print(f"Consumer {consumer_id} Consumed: {item}")
        q.task_done()

try:
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))
    num_items = int(input("Enter the number of items per producer: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    #sys.exit(1)

q = queue.Queue()

producers = [threading.Thread(target=producer, args=(q, i, num_items)) for i in range(num_producers)]
consumers = [threading.Thread(target=consumer, args=(q, i, num_items)) for i in range(num_consumers)]

for producer in producers:
    producer.start()

for consumer in consumers:
    consumer.start()

for producer in producers:
    producer.join()

q.join()  # Wait for all items to be processed
for _ in consumers:
    q.put(None)  # Signal consumers to stop
for consumer in consumers:
    consumer.join()

print("All producers and consumers have finished.")