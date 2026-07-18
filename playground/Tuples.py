# 1. Creation
point = (10, 20)
single = (5,)               # MUST have a comma for a single-element tuple!

# 2. Unpacking (Massively useful in DSA)
x, y = point                # x = 10, y = 20

# 3. Operations (No mutation allowed)
# point[0] = 15             # ERROR! Tuples are immutable.
print(point[0])             # 10 (Access is O(1))