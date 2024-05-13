from typing import Any

def num_island(grid: list[list[str]]) -> int:
    
    def dfs(i: int, j: int) -> Any:
        # 조건에 따라 들어가고 탐색하기 
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid) or \
                grid[i][j] != "1":
                    return 

        grid[i][j] = "#"
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for load in range(len(grid)):
        for g in range(len(grid[0])):
            if grid[load][g] == "1":
                dfs(load, g)
                count += 1
    
    return count

data = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(num_island(data))



