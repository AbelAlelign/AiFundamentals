import heapq
from graph_data import graph, heuristic
from utils import reconstruct

def a_star(start, goal):
    pq = [(heuristic[start], start)]  # priority queue storing (f = g + h, node)
    g_cost = {start: 0}  # cost from start to each node
    parent = {start: None}  # stores path

    while pq:
        f, node = heapq.heappop(pq)  # get node with lowest f value

        if node == goal:
            return reconstruct(parent, goal), g_cost[node]  # return path and cost

        for neighbor, weight in graph[node]:
            new_g = g_cost[node] + weight  # calculate new cost from start

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g  # update cost
                f_score = new_g + heuristic[neighbor]  # f = g + h
                parent[neighbor] = node  # update path
                heapq.heappush(pq, (f_score, neighbor))  # push to queue

    return None, float("inf")  # if no path found


if __name__ == "__main__":
    path, cost = a_star('A', 'G')
    print("A* Path:", path)
    print("Total Cost:", cost)