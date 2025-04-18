# 给你一个下标从 0 开始的二维整数数组 questions ，其中 questions[i] = [pointsi, brainpoweri] 。 
# 
#  这个数组表示一场考试里的一系列题目，你需要 按顺序 （也就是从问题 0 开始依次解决），针对每个问题选择 解决 或者 跳过 操作。解决问题 i 将让你 获
# 得 pointsi 的分数，但是你将 无法 解决接下来的 brainpoweri 个问题（即只能跳过接下来的 brainpoweri 个问题）。如果你跳过问题 
# i ，你可以对下一个问题决定使用哪种操作。 
# 
#  
#  比方说，给你 questions = [[3, 2], [4, 3], [4, 4], [2, 5]] ： 
#  
# 
#  
#  如果问题 0 被解决了， 那么你可以获得 3 分，但你不能解决问题 1 和 2 。 
#  如果你跳过问题 0 ，且解决问题 1 ，你将获得 4 分但是不能解决问题 2 和 3 。 
#  
#  
# 
# 
#  请你返回这场考试里你能获得的 最高 分数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：questions = [[3,2],[4,3],[4,4],[2,5]]
# 输出：5
# 解释：解决问题 0 和 3 得到最高分。
# - 解决问题 0 ：获得 3 分，但接下来 2 个问题都不能解决。
# - 不能解决问题 1 和 2
# - 解决问题 3 ：获得 2 分
# 总得分为：3 + 2 = 5 。没有别的办法获得 5 分或者多于 5 分。
#  
# 
#  示例 2： 
# 
#  输入：questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# 输出：7
# 解释：解决问题 1 和 4 得到最高分。
# - 跳过问题 0
# - 解决问题 1 ：获得 2 分，但接下来 2 个问题都不能解决。
# - 不能解决问题 2 和 3
# - 解决问题 4 ：获得 5 分
# 总得分为：2 + 5 = 7 。没有别的办法获得 7 分或者多于 7 分。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= questions.length <= 10⁵ 
#  questions[i].length == 2 
#  1 <= pointsi, brainpoweri <= 10⁵ 
#  
# 
#  Related Topics 数组 动态规划 👍 168 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            point, brain = questions[i]
            dp[i] = max(dp[i + 1], point + dp[min(n, i + brain + 1)])
        return dp[0]
# leetcode submit region end(Prohibit modification and deletion)
