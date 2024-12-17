# 5 stars
def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    possible_places = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                for di, dj in possible_places:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        result[ni][nj] += 1
  
    return result
