def manhattan_distance(p1, p2):
    # p1 and p2 are tuples, e.g., (x, y)
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


# Test it
print(manhattan_distance((1, 2), (4, 6)))  # Output: 7