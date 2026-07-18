arr = [5, 2, 9, 1]

# 1. Ascending Sort
arr.sort()
print(arr)

# 2. Reverse (Descending) Sort
arr.sort(reverse=True)
print(arr)
arr = [5, 2, 9, 1]
# 3. Custom Sorting with Lambda
# Example: Sort strings by length, then alphabetically
words = ["banana", "apple", "kiwi", "pear"]
words.sort(key=lambda x: (len(x), x))
print(words)