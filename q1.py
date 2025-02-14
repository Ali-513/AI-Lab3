from collections import deque

def shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start = (1, 1)  
    end = (4, 4)    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    queue = deque([(start, [start])]) 
    visited = set([start])  
    while queue:
        (current, path) = queue.popleft()

        if current == end:
            return path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]

            if 1 <= next_row <= rows and 1 <= next_col <= cols and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                queue.append(((next_row, next_col), path + [(next_row, next_col)]))

    return None  


matrix = [[0 for _ in range(5)] for _ in range(5)] 
path = shortest_path(matrix)
print(path)
