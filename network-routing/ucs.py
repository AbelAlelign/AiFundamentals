import heapq
from graph_data import graph
from utils import reconstruct

def ucs(start, goal):
    pq = [(0, start)]  # priority queue storing (cost, node)
    cost = {start: 0}  # stores lowest cost to reach each node
    parent = {start: None}  # stores path (who leads to who)

    while pq:
        g, node = heapq.heappop(pq)  # get node with smallest cost

        if node == goal:
            return reconstruct(parent, goal), g  # return path and total cost

        for neighbor, weight in graph[node]:
            new_cost = g + weight  # calculate cost to neighbor

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost  # update cost
                parent[neighbor] = node  # update path
                heapq.heappush(pq, (new_cost, neighbor))  # push to queue

    return None, float("inf")  # if no path found


if __name__ == "__main__":
    path, cost = ucs('A', 'G')
    print("UCS Path:", path)
    print("Total Cost:", cost)