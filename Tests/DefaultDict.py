from collections import defaultdict

# Example: Building an adjacency list for a Graph
graph = defaultdict(list)
graph["node_A"].append("node_B") # No need to check if "node_A" exists!
print(graph)
# Example: Grouping by a default int (0)
scores = defaultdict(int)
scores["Alice"] += 10
print(scores)