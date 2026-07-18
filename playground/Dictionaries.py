map = {"Alice": 25, "Bob": 30}

# 1. Adding / Updating
map["Charlie"] = 35         # Put: O(1)
print(map)
map.update({"Dave": 40})    # Bulk update: O(K)
print(map)

# 2. Retrieving
age = map["Alice"]          # Unsafe retrieval (throws KeyError if missing)
print(age)
age = map.get("Dave", 0)    # Safe Retrieval (Returns default 0 if not found)
print(age)
# 3. Removing
del map["Bob"]              # Deletes key (throws KeyError if missing)
print(map)
val = map.pop("Alice")      # Removes key AND returns its value
print(val)
map.pop("Eve", None)        # Safe pop (returns None instead of throwing KeyError)
print(map)

# 4. Iteration
keys = map.keys()           # View of keys
vals = map.values()         # View of values
for key, val in map.items():# Iterate both!
    print(f"{key} is {val}")