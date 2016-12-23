class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = 0
        for i in xrange(len(grid)):
            for j in xrange (len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        length += 1
                    if j == 0 or grid[i][j-1] == 0:
                        length += 1
                    if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                        length += 1
                    if i == len(grid) - 1 or grid[i+1][j] == 0:
                        length += 1
        return length
