from collections import Counter

# Instantly count frequencies of an array or string
counts = Counter([1, 1, 2, 3, 3, 3])
print(counts[3])       # Returns 3
print(counts[99])      # Returns 0 (No KeyError!)
print(counts.most_common(1)) # Returns [(3, 3)]