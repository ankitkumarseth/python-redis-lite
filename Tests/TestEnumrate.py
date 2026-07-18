names = ["Alice", "Bob"]
scores = [100, 95]

# enumerate gives you both index and value safely
for i, name in enumerate(names):
    print(f"Index {i} is {name}")

# zip lets you iterate multiple arrays in parallel simultaneously
for name, score in zip(names, scores):
    print(f"{name} scored {score}")