# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 5596 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        # 双指针，遍历left,right左右指针，并维持左右最高墙left_max,right_max
        # 移动矮的指针，如果<对应最高墙的话，可以对应蓄水，否则更新对应最高墙
        left=0
        right=len(height)-1
        left_max,right_max=0,0
        trap=0
        while left<right:
            if height[left]<height[right]:
                if height[left]<left_max:
                    trap=trap+left_max-height[left]
                else:
                    left_max=height[left]
                left=left+1
            else:
                if height[right]<right_max:
                    trap=trap+right_max-height[right]
                else:
                    right_max=height[right]
                right=right-1
        return trap
        """
        # 单调栈，构造递减栈，栈内存放索引，栈内前两个元素对应底和左墙
        # 遍历元素大于栈顶，当前遍历元素为右墙，弹出栈顶为底，构成蓄水池，计算蓄水量后，循环至当前元素入栈形成递减栈
        stack=list()
        trap=0
        for i,h in enumerate(height):
            while stack and h>height[stack[-1]]:
                bottom=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                trap=trap+(min(height[left],h)-height[bottom])*(i-1-left)
            stack.append(i)
        return trap
# leetcode submit region end(Prohibit modification and deletion)
