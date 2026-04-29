import heapq
from graph_data import graph, heuristic
from utils import reconstruct

def a_star(start, goal):
    pq = [(heuristic[start], start)]
    g_cost = {start: 0}
    parent = {start: None}

    while pq:
        f, node = heapq.heappop(pq)

        if node == goal:
            return reconstruct(parent, goal), g_cost[node]

        for neighbor, weight in graph[node]:
            new_g = g_cost[node] + weight

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_score = new_g + heuristic[neighbor]
                parent[neighbor] = node
                heapq.heappush(pq, (f_score, neighbor))

    return None, float("inf")


if __name__ == "__main__":
    path, cost = a_star('A', 'G')
    print("A* Path:", path)
    print("Total Cost:", cost)