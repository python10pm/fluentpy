'''
Besides deque, other Python standard library packages implement queues:
queue
This provides the synchronized (i.e., thread-safe) classes Queue, 
LifoQueue, and PriorityQueue. These are used for safe communication between threads. 
All three classes can be bounded by providing a maxsize argument greater than 0 to the constructor. 
However, they don’t discard items to make room as deque does. In‐ stead, when the queue is full the 
insertion of a new item blocks—i.e., it waits until some other thread makes room by taking an item 
from the queue, which is useful to throttle the number of live threads.

multiprocessing
Implements its own bounded Queue, very similar to queue.Queue but designed for interprocess communication. 
A specialized multiprocessing.JoinableQueue is also available for easier task management.

asyncio
Newly added to Python 3.4, asyncio provides Queue, LifoQueue, PriorityQueue, and JoinableQueue with 
APIs inspired by the classes contained in the queue and multiprocessing modules, but adapted 
for managing tasks in asynchronous pro‐ gramming.

heapq
In contrast to the previous three modules, heapq does not implement a queue class, 
but provides functions like heappush and heappop that let you use a mutable 
se‐quence as a heap queue or priority queue.
'''
from collections import deque

dq = deque(range(10), maxlen = 10)

if __name__ == "__main__":
    print(dq)
    print("Returning None because it makes the extend inplace")
    print(dq.extendleft([10, 10, 3]))
    print(dq)
    print(dq.rotate(5))
    print(dq)