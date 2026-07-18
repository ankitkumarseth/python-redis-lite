# The Ultimate Python Cheatsheet (For Java Developers)

Welcome to your central hub for Python mastery. If you are ever stuck on "how do I do X in Python that I used to do in Java?", this is your reference.

---

## 1. The Absolute Basics

### Variables & Typing
Python is dynamically typed. You don't declare types, but you *can* use type hints for readability (highly recommended for production code).

```python
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
squares = [n * n for n in nums if n % 2 == 0] # [4, 16]
```

---

## 3. Functions & Arguments (`*args`)

Python functions are incredibly flexible.
```python
# 1. Default arguments
def greet(name="Guest"):
    print(f"Hello {name}")

# 2. Packing / Unpacking (*args)
# *args allows you to pass any number of positional arguments.
def mset(*args):
    # args is a tuple of all passed arguments
    print(args) 

mset("key1", "val1", "key2", "val2") # prints: ("key1", "val1", "key2", "val2")
```

---

## 4. Object-Oriented Programming & Dunder Methods

Python OOP is fundamentally identical to Java, but with simpler syntax. 
- There is no `public/private` (we use a leading underscore `_` to signal "private by convention").
- `this` is called `self`, and you MUST pass it explicitly as the first argument to instance methods.

### Dunder (Double Underscore) Methods
These are magic methods that let your objects behave like built-in Python types.
```python
class Database:
    def __init__(self):
        self.store = {"A": 1, "B": 2}
        
    def __len__(self):
        # Allows you to call `len(db)`!
        return len(self.store)
        
    def __str__(self):
        # Equivalent to Java's `toString()`
        return f"Database with {len(self)} items"

db = Database()
print(len(db)) # 2
print(db)      # "Database with 2 items"
```

---

## 5. Core Data Structures (The DSA Toolbelt)

### Lists (Java `ArrayList`)
Python lists are highly versatile. Here are the core methods you need to know for DSA:

```python
arr = [10, 20, 30]

# 1. Adding Elements
arr.append(40)          # Adds 40 to the end: O(1)
arr.insert(1, 15)       # Inserts 15 at index 1 (shifts rest right): O(N)
arr.extend([50, 60])    # Appends multiple elements to the end: O(K)

# 2. Removing Elements
arr.pop()               # Removes & returns the LAST element: O(1)
popped = arr.pop(1)     # Removes & returns element at index 1: O(N)
arr.remove(20)          # Removes the FIRST occurrence of value 20: O(N)
del arr[0]              # Deletes element at index 0 without returning it: O(N)

# 3. Sorting (Mutating vs Non-Mutating)
arr.sort()              # Mutates the list in-place (returns None)
new_arr = sorted(arr)   # Creates a BRAND NEW sorted list (arr remains unchanged)
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
```

### Dictionaries (Java `HashMap`)
Dictionaries are Python's Hash Maps. They store key-value pairs and offer $O(1)$ lookups.

```python
map = {"Alice": 25, "Bob": 30}

# 1. Adding / Updating
map["Charlie"] = 35         # Put: O(1)
map.update({"Dave": 40})    # Bulk update: O(K)

# 2. Retrieving
age = map["Alice"]          # Unsafe retrieval (throws KeyError if missing)
age = map.get("Dave", 0)    # Safe Retrieval (Returns default 0 if not found)

# 3. Removing
del map["Bob"]              # Deletes key (throws KeyError if missing)
val = map.pop("Alice")      # Removes key AND returns its value
map.pop("Eve", None)        # Safe pop (returns None instead of throwing KeyError)

# 4. Iteration
keys = map.keys()           # View of keys
vals = map.values()         # View of values
for key, val in map.items():# Iterate both!
    print(f"{key} is {val}")
```

### Advanced Collections (The DSA Secret Weapons)
If you are doing frequency counts or grouping elements, **do not** use a normal dictionary. Use these imports from `collections` to save yourself from writing boilerplate `if key in map:` logic.

**1. `Counter` (Frequency Counting)**
```python
from collections import Counter

# Instantly count frequencies of an array or string
counts = Counter([1, 1, 2, 3, 3, 3]) 
print(counts[3])       # Returns 3
print(counts[99])      # Returns 0 (No KeyError!)
print(counts.most_common(1)) # Returns [(3, 3)]
```

**2. `defaultdict` (Grouping / Graph Adjacency Lists)**
```python
from collections import defaultdict

# Example: Building an adjacency list for a Graph
graph = defaultdict(list)
graph["node_A"].append("node_B") # No need to check if "node_A" exists!

# Example: Grouping by a default int (0)
scores = defaultdict(int)
scores["Alice"] += 10
```

### Common Built-in Utilities
*   `max(arr)`, `min(arr)`, `sum(arr)`: Instantly compute aggregates.
*   `any(condition for x in arr)`: Returns `True` if *at least one* element matches.
*   `all(condition for x in arr)`: Returns `True` if *every* element matches.

### Tuples (Immutable Lists)
Tuples are just like lists, but they are **immutable** (cannot be changed after creation). This makes them perfect for storing coordinate pairs `(x, y)` or using them as keys in a Dictionary!

```python
# 1. Creation
point = (10, 20)
single = (5,)               # MUST have a comma for a single-element tuple!

# 2. Unpacking (Massively useful in DSA)
x, y = point                # x = 10, y = 20

# 3. Operations (No mutation allowed)
# point[0] = 15             # ERROR! Tuples are immutable.
print(point[0])             # 10 (Access is O(1))
```

### Sets (Java `HashSet`)
Sets store unique elements and offer $O(1)$ lookups. They support powerful mathematical operations.

```python
seen = set([1, 2, 3])

# 1. Adding / Checking
seen.add(4)                 # Add element: O(1)
print(2 in seen)            # Check existence: True: O(1)

# 2. Removing
seen.remove(4)              # Removes 4 (throws KeyError if missing)
seen.discard(99)            # Safely removes 99 (does nothing if missing)

# 3. Set Operations (Math logic)
setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA & setB)          # Intersection: {3}
print(setA | setB)          # Union: {1, 2, 3, 4, 5}
print(setA - setB)          # Difference: {1, 2}
print(setA ^ setB)          # Symmetric Diff (In A or B, but not both): {1, 2, 4, 5}

setA.difference_update(setB)# In-place Difference (Mutates setA to {1, 2})
```

### Heaps / Priority Queues (Java `PriorityQueue`)
Python's `heapq` is a **Min-Heap** by default. It transforms a normal list into a heap in-place.

```python
import heapq

# 1. Standard Min-Heap (Smallest value treated first)
min_heap = []
heapq.heappush(min_heap, 50)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 99)
smallest = heapq.heappop(min_heap)  # Returns 10

# 2. Max-Heap Trick (Largest value treated first)
# Multiply by -1 before pushing, and -1 again after popping
max_heap = []
heapq.heappush(max_heap, 50 * -1)
heapq.heappush(max_heap, 10 * -1)
heapq.heappush(max_heap, 99 * -1)
largest = heapq.heappop(max_heap) * -1  # Returns 99

# 3. Heapify an existing array: O(N) time!
arr = [9, 3, 2, 7]
heapq.heapify(arr) # Mutates arr into a valid heap in-place
```

---

## 6. Sorting (Advanced)

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
```

---

## 7. Bitwise Operations

### Part A: The Fundamentals
You must understand what the operators do to binary strings.
*Let's assume A = 5 (0101 in binary) and B = 3 (0011 in binary).*

*   **AND (`&`):** Returns 1 if *both* bits are 1. (`5 & 3` = `1`)
*   **OR (`|`):** Returns 1 if *either* bit is 1. (`5 | 3` = `7`)
*   **XOR (`^`):** Returns 1 if bits are *different*. (`5 ^ 3` = `6`)
*   **NOT (`~`):** Flips all bits. `~5` = `-6`
*   **Left Shift (`<<`):** Shifts bits left (multiplies by 2). `5 << 1` = `10`
*   **Right Shift (`>>`):** Shifts bits right (floor division by 2). `5 >> 1` = `2`

### Part B: The 4 Essential Tricks
```python
# 1. The XOR Trick: A ^ A = 0
print(5 ^ 5)  # 0

# 2. Checking Even/Odd
n = 5
is_odd = (n & 1) == 1

# 3. Multiply / Divide by 2 instantly
val = 10 << 1 # 20

# 4. Clear the lowest set bit (Brian Kernighan’s algorithm)
n = 10 # 1010
n = n & (n - 1) # 1000 (8)
```

---

## 8. File Handling (The Pythonic Way)

Unlike Java's `BufferedReader`, Python uses `with open()` which automatically safely closes the file.

```python
with open('data.txt', 'r') as file:
    content = file.read()       

with open('output.txt', 'w') as file:
    file.write("Hello World!\\n")
```
