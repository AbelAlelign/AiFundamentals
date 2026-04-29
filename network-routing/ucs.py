import heapq
from graph_data import graph
from utils import reconstruct

def ucs(start, goal):
    pq = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    while pq:
        g, node = heapq.heappop(pq)

        if node == goal:
            return reconstruct(parent, goal), g

        for neighbor, weight in graph[node]:
            new_cost = g + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    return None, float("inf")


if __name__ == "__main__":
    path, cost = ucs('A', 'G')
    print("UCS Path:", path)
    print("Total Cost:", cost)