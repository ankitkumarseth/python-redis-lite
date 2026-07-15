# The Ultimate Python Cheatsheet (For Java Developers)

Welcome to your central hub for Python mastery. If you are ever stuck on "how do I do X in Python that I used to do in Java?", this is your reference.

---

## 1. The Absolute Basics

### Variables & Typing
Python is dynamically typed. You don't declare types, but you *can* use type hints for readability (highly recommended for production code).

```python
# Java: String name = "Alice"; int age = 30;
name: str = "Alice"
age: int = 30
is_active: bool = True  # Note: True/False are capitalized!
nothing: None = None    # Python's version of 'null'
```

### Initializing Min/Max (DSA Pro-Tip)
In Java you use `Integer.MAX_VALUE`. In Python, you use infinity.
```python
max_val = float('inf')
min_val = float('-inf')
```

### Exceptions
Python uses `try` / `except` (instead of `try` / `catch`).
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
finally:
    print("Always runs")
```

---

## 2. Iteration & "Pythonic" Sugar

### The Power of `enumerate` and `zip`
Never use `for i in range(len(arr))` if you also need the value!
```python
names = ["Alice", "Bob"]
scores = [100, 95]

# enumerate gives you both index and value safely
for i, name in enumerate(names):
    print(f"Index {i} is {name}")

# zip lets you iterate multiple arrays in parallel simultaneously
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

### Slicing `[start:stop:step]`
You can slice arrays and strings effortlessly.
```python
s = "Mastercard"
print(s[0:6])   # 'Master' (Index 0 to 5)
print(s[-4:])   # 'card' (Last 4 characters)
print(s[::-1])  # 'dracretsaM' (Reverses the string!)
```

### List Comprehensions
Transform data in one line.
```python
nums = [1, 2, 3, 4]
# Java: List<Integer> sq = new ArrayList<>(); for(int n: nums){ sq.add(n*n); }
squares = [n * n for n in nums if n % 2 == 0] # [4, 16]
```

---

## 3. Core Data Structures (The DSA Toolbelt)

### Lists (Java `ArrayList`)
```python
arr = [10, 20, 30]
arr.append(40)      # Add to end: O(1)
arr.pop()           # Remove from end: O(1)
# arr.pop(0)        # DO NOT DO THIS! It shifts all elements: O(N)
```

### Queues / Deques (Java `LinkedList`)
If you need a Queue for BFS, **always use `collections.deque`**. 
```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)       # Enqueue to tail: O(1)
queue.appendleft(0)   # Enqueue to head: O(1)
queue.popleft()       # Dequeue from head: O(1)
queue.pop()           # Dequeue from tail: O(1)

# Advanced Trick: Rotating the queue
queue.rotate(1)       # Shifts elements 1 step to the right (circular)
```

### Dictionaries (Java `HashMap`)
```python
map = {"Alice": 25, "Bob": 30}
map["Charlie"] = 35         # Put: O(1)

# Safe Retrieval (Avoids KeyError)
age = map.get("Dave", 0)    # Returns 0 if "Dave" is not found

# Iterating
for key, val in map.items():
    pass
```

#### Advanced HashMaps (DSA Cheats)
```python
from collections import defaultdict, Counter

# 1. defaultdict: Automatically handles missing keys
adj_list = defaultdict(list)
adj_list["node_A"].append("node_B")  # Initializes empty list instantly

# 2. Counter: Counts frequencies instantly.
freq = Counter(["apple", "apple", "banana"])
print(freq["apple"])  # 2
```

### Sets (Java `HashSet`)
```python
seen = set([1, 2, 3])
seen.add(4)
print(2 in seen) # True: O(1)
```

### Heaps / Priority Queues (Java `PriorityQueue`)
Python's `heapq` is a **Min-Heap** by default. It transforms a normal list into a heap in-place.
```python
import heapq

# 1. Creating a heap from scratch
min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
smallest = heapq.heappop(min_heap)  # Returns 5

# 2. Heapify an existing array: O(N) time!
arr = [9, 3, 2, 7]
heapq.heapify(arr) 

# 3. Max-Heap Trick: Multiply by -1
max_heap = []
heapq.heappush(max_heap, -10)
largest = -1 * heapq.heappop(max_heap) # Returns 10

# 4. Top K elements (Very useful!)
top_two = heapq.nlargest(2, [9, 3, 2, 7])   # [9, 7]
bottom_two = heapq.nsmallest(2, [9, 3, 2, 7]) # [2, 3]
```

---

## 4. Sorting (Advanced)

Sorting is a critical operation in many algorithms.
```python
arr = [5, 2, 9, 1]

# 1. Ascending Sort
arr.sort()

# 2. Reverse (Descending) Sort
arr.sort(reverse=True)

# 3. Custom Sorting with Lambda
# Example: Sort strings by length, then alphabetically
words = ["banana", "apple", "kiwi", "pear"]
words.sort(key=lambda x: (len(x), x)) 
# Result: ['kiwi', 'pear', 'apple', 'banana']
```

---

## 5. Bitwise Operations

### Part A: The Fundamentals
You must understand what the operators do to binary strings before using them in algorithms.
*Let's assume A = 5 (0101 in binary) and B = 3 (0011 in binary).*

*   **AND (`&`):** Returns 1 if *both* bits are 1.
    *   `5 & 3` (0101 & 0011) = `0001` (1)
*   **OR (`|`):** Returns 1 if *either* bit is 1.
    *   `5 | 3` (0101 | 0011) = `0111` (7)
*   **XOR (`^`):** Returns 1 if bits are *different*. Returns 0 if they are the *same*.
    *   `5 ^ 3` (0101 ^ 0011) = `0110` (6)
*   **NOT (`~`):** Flips all bits. (In Python, `~x` returns `-(x+1)` due to two's complement).
    *   `~5` = `-6`
*   **Left Shift (`<<`):** Shifts bits to the left, filling with 0s. (Equivalent to multiplying by 2).
    *   `5 << 1` (0101 -> 1010) = `10`
*   **Right Shift (`>>`):** Shifts bits to the right. (Equivalent to floor division by 2).
    *   `5 >> 1` (0101 -> 0010) = `2`

### Part B: The 4 Essential Tricks

```python
# 1. The XOR Trick: A ^ A = 0, and A ^ 0 = A
# Use Case: Find the missing/unique number in an array.
print(5 ^ 5)  # 0

# 2. Checking Even/Odd
# The last bit of any odd number is always 1.
n = 5
is_odd = (n & 1) == 1

# 3. Multiply / Divide by 2 instantly
val = 10
val = val << 1 # 20
val = val >> 1 # 10

# 4. Clear the lowest set bit (Brian Kernighan’s algorithm)
# Use Case: Counting the number of 1s in a binary string.
n = 10 # 1010
n = n & (n - 1) # Clears the right-most '1', resulting in 1000 (8)
```

---

## 6. File Handling (The Pythonic Way)

Unlike Java's verbose `BufferedReader`, Python uses the `with open()` context manager which automatically safely closes the file for you (even if exceptions occur). This directly maps to **Chapter 7** of the IITM syllabus.

```python
# 1. Reading a file
with open('data.txt', 'r') as file:
    content = file.read()       # Read entire file
    # Or iterate line by line (highly memory efficient):
    # for line in file:
    #     print(line.strip())

# 2. Writing to a file (overwrites)
with open('output.txt', 'w') as file:
    file.write("Hello World!\\n")

# 3. Appending to a file
with open('log.txt', 'a') as file:
    file.write("New log entry\\n")
```
