# 给你两个整数 n 和 k 。 
# 
#  对于一个由 不同 正整数组成的数组，如果其中不存在任何求和等于 k 的不同元素对，则称其为 k-avoiding 数组。 
# 
#  返回长度为 n 的 k-avoiding 数组的可能的最小总和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 5, k = 4
# 输出：18
# 解释：设若 k-avoiding 数组为 [1,2,4,5,6] ，其元素总和为 18 。
# 可以证明不存在总和小于 18 的 k-avoiding 数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2, k = 6
# 输出：3
# 解释：可以构造数组 [1,2] ，其元素总和为 3 。
# 可以证明不存在总和小于 3 的 k-avoiding 数组。 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n, k <= 50 
#  
# 
#  Related Topics 贪心 数学 👍 44 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        avoid = set()
        ans = 0
        for i in range(1, k):
            if i in avoid:
                continue
            ans += i
            n -= 1
            if n == 0:
                return ans
            avoid.add(k - i)
        return ans + sum(range(k, k + n))
# leetcode submit region end(Prohibit modification and deletion)
