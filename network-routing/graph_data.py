# Network graph (routers and latency)
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 4), ('E', 7)],
    'C': [('A', 5), ('F', 6)],
    'D': [('B', 4), ('G', 2)],
    'E': [('B', 7), ('G', 3)],
    'F': [('C', 6), ('G', 1)],
    'G': []
}

# Heuristic values (estimated distance to goal G)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 1,
    'G': 0
}