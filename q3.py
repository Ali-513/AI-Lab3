from queue import PriorityQueue

graph = {
    "The": [("cat", 2), ("dog", 3)],
    "cat": [("runs", 1)],
    "dog": [("runs", 2)],
    "runs": [("fast", 2)],
    "fast": []
}

heuristic = {
    "The": 4,
    "cat": 3,
    "dog": 3,
    "runs": 2,
    "fast": 1
}

def a_star_algorithm(start, goal):
    open_list = PriorityQueue()
    open_list.put((0 + heuristic[start], start))
    came_from = {}
    cost_so_far = {start: 0}

    while not open_list.empty():
        _, current_node = open_list.get()

        if current_node == goal:
            break

        for neighbor, cost in graph[current_node]:
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                open_list.put((priority, neighbor))
                came_from[neighbor] = current_node

    path = []
    current = goal
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path, cost_so_far[goal]

start_node = "The"
goal_node = "fast"
path, total_cost = a_star_algorithm(start_node, goal_node)
print(f"Optimal path: {path}")
print(f"Total cost: {total_cost}")
