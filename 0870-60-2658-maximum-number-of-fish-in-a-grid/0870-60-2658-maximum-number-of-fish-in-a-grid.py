class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                res = max(res, self.search(i, j, grid, visited))
        return res
    
    def search(self, i, j, grid, visited): 
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0: 
            return 0
        if grid[i][j] == 0 or (i, j) in visited: 
            return 0 
        feesh = grid[i][j]
        visited.add((i, j))

        #search 
        feesh += self.search(i, j + 1, grid, visited)
        feesh += self.search(i, j - 1, grid, visited)
        feesh += self.search(i + 1, j, grid, visited)
        feesh += self.search(i - 1, j, grid, visited)

        return feesh 