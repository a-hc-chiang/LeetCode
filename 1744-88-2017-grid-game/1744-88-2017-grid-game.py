class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row1sums = []
        row2sums = []
        n = len(grid[0])

        row1runningSum = 0
        row2runningSum = 0
        for i in range(n):
            row1runningSum += grid[0][-i - 1]
            row2runningSum += grid[1][i]
            row1sums.append(row1runningSum)
            row2sums.append(row2runningSum)

        row1sums = row1sums[::-1]

        currMax = float('inf')

        for i in range(n):
            top_remaining = row1sums[i + 1] if i + 1 < n else 0
            bottom_remaining = row2sums[i - 1] if i > 0 else 0
            currMax = min(currMax, max(top_remaining, bottom_remaining))
        
        return currMax
