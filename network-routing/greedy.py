import heapq
from graph_data import graph, heuristic
from utils import reconstruct

def greedy_best_first(start, goal):
    pq = [(heuristic[start], start)]
    visited = set()
    parent = {start: None}

    while pq:
        h, node = heapq.heappop(pq)

        if node == goal:
            return reconstruct(parent, goal)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return None


if __name__ == "__main__":
    path = greedy_best_first('A', 'G')
    print("Greedy Path:", path)