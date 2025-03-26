# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 2726 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            grid[x][y] = "0"
            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= x + a < row_num and 0 <= y + b < col_num and grid[x + a][y + b] == "1":
                    dfs(x + a, y + b)

        res = 0
        row_num = len(grid)
        col_num = len(grid[0])
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution.numIslands(Solution(), [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
