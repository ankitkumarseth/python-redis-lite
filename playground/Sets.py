seen = set([1, 2, 3])

# 1. Adding / Checking
seen.add(4)                 # Add element: O(1)
print(seen)
print(2 in seen)            # Check existence: True: O(1)

# 2. Removing
seen.remove(4)              # Removes 4 (throws KeyError if missing)
print(seen)
seen.discard(99)            # Safely removes 99 (does nothing if missing)
print(seen)

# 3. Set Operations (Math logic)
setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA & setB)          # Intersection: {3}
print(setA | setB)          # Union: {1, 2, 3, 4, 5}
print(setA - setB)          # Difference: {1, 2}
print(setA ^ setB)          # Symmetric Diff (In A or B, but not both): {1, 2, 4, 5}

setA.difference_update(setB)# In-place Difference (Mutates setA to {1, 2})
print(setA)