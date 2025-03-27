# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 3806 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = []

        def dfs(l, r):
            if len(tmp) == 2 * n:
                res.append(''.join(tmp))
                return
            if l < n:
                tmp.append('(')
                dfs(l + 1, r)
                tmp.pop()
            if r < l:
                tmp.append(')')
                dfs(l, r + 1)
                tmp.pop()

        dfs(0, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
