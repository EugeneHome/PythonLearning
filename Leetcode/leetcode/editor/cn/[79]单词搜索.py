# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "ABCCED"
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "SEE"
# 输出：true
#  
# 
#  示例 3： 
#  
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "ABCB"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？ 
# 
#  Related Topics 深度优先搜索 数组 字符串 回溯 矩阵 👍 1965 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        first = list()
        for i in range(m):
            for j in range(n):
                if board[i][j] not in word:
                    board[i][j] = None
                if board[i][j] == word[0]:
                    first.append([i, j])
        if not first:
            return False
        l = len(word)
        res = False
        arround = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, k):
            nonlocal res
            if k == l:
                res = True
                return
            for x, y in arround:
                if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == word[k]:
                    tmp = board[i + x][j + y]
                    board[i + x][j + y] = None
                    dfs(i + x, j + y, k + 1)
                    board[i + x][j + y] = tmp

        for i, j in first:
            tmp = board[i][j]
            board[i][j] = None
            dfs(i, j, 1)
            board[i][j] = tmp
        return res
# leetcode submit region end(Prohibit modification and deletion)
