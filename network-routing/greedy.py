import heapq
from graph_data import graph, heuristic
from utils import reconstruct

def greedy_best_first(start, goal):
    pq = [(heuristic[start], start)]  # priority queue storing (heuristic, node)
    visited = set()  # keeps track of visited nodes
    parent = {start: None}  # stores path

    while pq:
        h, node = heapq.heappop(pq)  # get node with lowest heuristic

        if node == goal:
            return reconstruct(parent, goal)  # return path

        if node in visited:
            continue  # skip if already visited

        visited.add(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node  # update path
                heapq.heappush(pq, (heuristic[neighbor], neighbor))  # push based on heuristic

    return None  # if no path found


if __name__ == "__main__":
    path = greedy_best_first('A', 'G')
    print("Greedy Path:", path)