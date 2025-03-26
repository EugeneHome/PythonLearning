# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
#  
# 
#  示例 2： 
#  
#  
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 300 
#  points[i].length == 2 
#  -10⁴ <= xi, yi <= 10⁴ 
#  points 中的所有点 互不相同 
#  
# 
#  Related Topics 几何 数组 哈希表 数学 👍 587 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)

        n = len(points)
        if n < 3:
            return n
        res = 1
        for i in range(n):
            ht = dict()
            tmp = 1
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x, y = x1 - x2, y1 - y2
                k = gcd(x, y)
                k = str(x // k) + "/" + str(y // k)
                ht[k] = ht.get(k, 1) + 1
                tmp = max(tmp, ht[k])
            res = max(res, tmp)
        return res
# leetcode submit region end(Prohibit modification and deletion)
