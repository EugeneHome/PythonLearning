# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  算法的时间复杂度应该为 O(log (m+n)) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
# 
#  Related Topics 数组 二分查找 分治 👍 7467 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(nums1, nums2, k):
            if len(nums1) == 0:
                return nums2[k - 1]
            if len(nums2) == 0:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])
            if k // 2 > len(nums2):
                return findKth(nums1[k // 2:], nums2, k - k // 2)
            if k // 2 > len(nums1):
                return findKth(nums1, nums2[k // 2:], k - k // 2)
            if nums1[k // 2 - 1] < nums2[k // 2 - 1]:
                return findKth(nums1[k // 2:], nums2, k - k // 2)
            else:
                return findKth(nums1, nums2[k // 2:], k - k // 2)

        n1, n2 = len(nums1), len(nums2)
        num1 = findKth(nums1, nums2, (n1 + n2 + 1) // 2)
        num2 = findKth(nums1, nums2, (n1 + n2) // 2 + 1)
        return (num1 + num2) / 2.0
# leetcode submit region end(Prohibit modification and deletion)
