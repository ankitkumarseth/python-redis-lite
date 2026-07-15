# The Ultimate Python Cheatsheet (For Java Developers)

Welcome to your central hub for Python mastery. If you are ever stuck on "how do I do X in Python that I used to do in Java?", this is your reference.

---

## 1. The Absolute Basics

### Variables & Typing
Python is dynamically typed. You don't declare types, but you *can* use type hints for readability (highly recommended for interviews).

```python
# Java: String name = "Alice";
#       int age = 30;
name: str = "Alice"
age: int = 30
is_active: bool = True  # Note: True/False are capitalized!
nothing: None = None    # Python's version of 'null'
```

### Control Flow (If / Else)
Python uses indentation (4 spaces) instead of curly braces `{}`.

```python
if age > 18:
    print("Adult")
elif age == 18:     # Java: else if (age == 18)
    print("Just 18")
else:
    print("Minor")
```

### Loops (For & While)
Forget `for (int i = 0; i < n; i++)`. In Python, you iterate over ranges or collections directly.

```python
# Loop from 0 to 4 (5 is exclusive)
for i in range(5):
    print(i)

# Loop backwards from 5 down to 1
for i in range(5, 0, -1):
    print(i)

# While loops remain exactly the same
count = 0
while count < 3:
    count += 1
```

### Functions
Use `def`. 

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
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

## 2. Strings & "Pythonic" Sugar

### F-Strings (String Interpolation)
Stop using `.format()` or string concatenation `+`. Use f-strings.
```python
name = "Ankit"
print(f"Hello {name}, your age is {age}.")
```

### Slicing `[start:stop:step]`
This is a superpower. You can slice arrays and strings effortlessly.
```python
s = "Mastercard"
print(s[0:6])   # 'Master' (Index 0 to 5)
print(s[-4:])   # 'card' (Last 4 characters)
print(s[::-1])  # 'dracretsaM' (Reverses the string!)
```

### List Comprehensions
Transform data in one line instead of a massive `for` loop.
```python
nums = [1, 2, 3, 4]
# Java: List<Integer> squares = new ArrayList<>(); for(int n: nums){ squares.add(n*n); }
squares = [n * n for n in nums]

# With a condition (Only even squares)
even_squares = [n * n for n in nums if n % 2 == 0]
```

---

## 3. Core Data Structures (The DSA Toolbelt)

### Lists (Java `ArrayList`)
Lists are dynamic arrays.
```python
arr = [10, 20, 30]
arr.append(40)      # Add to end: O(1)
arr.pop()           # Remove from end: O(1)
arr.pop(0)          # Remove from start: O(N) -> DO NOT USE THIS FOR QUEUES!
```

### Queues / Deques (Java `LinkedList`)
If you need a Queue for BFS, **always use `collections.deque`**. 
```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)     # Enqueue: O(1)
queue.popleft()     # Dequeue: O(1)
```

### Dictionaries (Java `HashMap`)
Dictionaries are ordered by insertion (since Python 3.7) and extremely fast.
```python
map = {"Alice": 25, "Bob": 30}
map["Charlie"] = 35         # Put: O(1)
print("Alice" in map)       # ContainsKey: O(1)
del map["Bob"]              # Remove: O(1)

# Iterating
for key, val in map.items():
    print(f"{key} -> {val}")
```

#### Advanced HashMaps (DSA Cheats)
```python
from collections import defaultdict, Counter

# 1. defaultdict: Never worry about NullPointerExceptions / KeyErrors again.
adj_list = defaultdict(list)
adj_list["node_A"].append("node_B")  # Automatically initializes "node_A" with an empty list!

# 2. Counter: Counts frequencies instantly.
freq = Counter([1, 1, 2, 2, 2, 3])
print(freq[2])  # Output: 3 (Because 2 appears 3 times)
```

### Sets (Java `HashSet`)
Unordered, unique elements. Fast lookups.
```python
seen = set()
seen.add(1)
seen.add(1)
print(seen)      # {1}
print(1 in seen) # True: O(1)
```

### Heaps / Priority Queues (Java `PriorityQueue`)
Python's `heapq` is a **Min-Heap** by default.
```python
import heapq

min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
smallest = heapq.heappop(min_heap)  # Returns 5

# Trick: To make a Max-Heap, multiply all values by -1 before pushing!
```

---

## 4. Object-Oriented Programming (Classes)

Python OOP is simpler than Java but fundamentally identical. 
- There is no `public/private` (we use a leading underscore `_` to signal "private by convention").
- `this` is called `self`, and you MUST pass it explicitly as the first argument to instance methods.
- The constructor is always named `__init__`.

```python
class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
        
    def display(self):
        print(f"Node value: {self.val}")

# Instantiation (no 'new' keyword)
head = Node(10)
head.display()
```

---

## 5. Sorting

In interviews, sorting is critical.
```python
arr = [5, 2, 9, 1]

# 1. In-place sort (modifies arr directly)
arr.sort()

# 2. Return a new sorted list (leaves original untouched)
new_arr = sorted(arr)

# 3. Custom sorting (Java Comparable/Comparator)
words = ["apple", "banana", "kiwi", "pear"]
# Sort by string length using a lambda function
words.sort(key=lambda x: len(x)) 
print(words) # ['kiwi', 'pear', 'apple', 'banana']
```

---

## 6. Bitwise Operations (The 4 Tricks)

Bitwise operations are mainly used in a specific subset of DSA problems.

```python
# 1. XOR (^)
# The rule: X ^ X = 0, and X ^ 0 = X
# Very useful for finding the "missing" or "unique" number in an array.
print(5 ^ 5)  # 0

# 2. Bitwise AND (&) 
# Commonly used to check if a number is even/odd.
# If the last bit is 1, it's odd.
n = 5
is_odd = (n & 1) == 1

# 3. Left Shift (<<) and Right Shift (>>)
# Left shift by 1 multiplies by 2. Right shift by 1 divides by 2.
print(4 << 1) # 8
print(4 >> 1) # 2

# 4. Clear the lowest set bit
# Used in Brian Kernighan’s algorithm to count bits.
n = n & (n - 1)
```

---

## 7. File Handling (The Pythonic Way)

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
