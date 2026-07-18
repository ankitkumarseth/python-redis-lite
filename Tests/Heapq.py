import heapq

# 1. Standard Min-Heap (Smallest value treated first)
min_heap = []
heapq.heappush(min_heap, 50)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 99)
smallest = heapq.heappop(min_heap)  # Returns 10
print(smallest)
print(min_heap)

# 2. Max-Heap Trick (Largest value treated first)
# Multiply by -1 before pushing, and -1 again after popping
max_heap = []
heapq.heappush(max_heap, 50 * -1)
heapq.heappush(max_heap, 10 * -1)
heapq.heappush(max_heap, 99 * -1)
largest = heapq.heappop(max_heap) * -1  # Returns 99
print(largest)
print(max_heap)

# 3. Heapify an existing array: O(N) time!
arr = [9, 3, 2, 7]
heapq.heapify(arr) # Mutates arr into a valid heap in-place
print(arr)