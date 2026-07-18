from collections import deque

queue = deque([1, 2, 3])
queue.append(4)       # Enqueue to tail: O(1)
print(queue)
queue.appendleft(0)   # Enqueue to head: O(1)
print(queue)
queue.popleft()       # Dequeue from head: O(1)
print(queue)
queue.pop()           # Dequeue from tail: O(1)
print(queue)