import time

# 1. Start the stopwatch
start_time = time.time()
#print(101 % 2 == 0)
print(100 & 1 == 0) # Check for even number
# 2. Stop the stopwatch
end_time = time.time()
# 3. Print the difference
print(f"Execution Time: {end_time - start_time:.5f} seconds")

