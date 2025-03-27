# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  
# 
#  Related Topics 回溯 👍 565 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        queens = []
        dale = []
        hill = []

        def dfs():
            y = len(queens)
            if y == n:
                res.append(queens.copy())
                return
            for x in range(n):
                if x not in queens and y - x not in dale and y + x not in hill:
                    queens.append(x)
                    dale.append(y - x)
                    hill.append(y + x)
                    dfs()
                    queens.pop()
                    dale.pop()
                    hill.pop()

        dfs()
        return len(res)
# leetcode submit region end(Prohibit modification and deletion)
