import numpy as np
import json
import random

N_SAMPLES = 100
data_list = []

def gen_island(height, width, p1):
    matrix = np.zeros((height, width), dtype=int)
    num_ones = int(height * width * p1)
    
    available_positions = set((i, j) for i in range(height) for j in range(width))

    def mark_diagonals(i, j):
        if i > 0 and j > 0:
            available_positions.discard((i - 1, j - 1))
        if i > 0 and j < width - 1:
            available_positions.discard((i - 1, j + 1))
        if i < height - 1 and j > 0:
            available_positions.discard((i + 1, j - 1))
        if i < height - 1 and j < width - 1:
            available_positions.discard((i + 1, j + 1))

    while num_ones > 0 and available_positions:
        i, j = random.sample(available_positions, 1)[0]
        matrix[i, j] = 1
        available_positions.discard((i, j))
        mark_diagonals(i, j)
        num_ones -= 1

    return matrix

def matrix2str(matrix):
    rows = []
    for row in matrix:
        rows.append(''.join('█' if cell == 1 else ' ' for cell in row))
    return '\n'.join(rows)

def island_solver(grid):
    if not grid.size:
        return 0
    
    height, width = grid.shape
    visited = np.zeros_like(grid, dtype=bool)
    
    def dfs(x, y):
        """ Depth-first search to mark all parts of an island as visited """
        if x < 0 or x >= height or y < 0 or y >= width or visited[x][y] or grid[x][y] == 0:
            return
        visited[x][y] = True
        # Explore neighbors (up, down, left, right)
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    island_count = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                island_count += 1
    
    return island_count

for _ in range(N_SAMPLES):
    island_sample = gen_island(7, 7, 0.5)
    answer = island_solver(island_sample)
    print(island_sample)
    island_sample = matrix2str(island_sample)
    question = f"Count the number of islands in a given 2D map, where black blocks represent land and spaces represent water. Output a single number as your result\nMap:\n{island_sample}"
    print(question)
    print(answer)
    data_list.append({"question": question, "answer": str(answer)})

# Write the data list to a JSON file
with open("search.json", "w") as f:
    json.dump(data_list, f)
