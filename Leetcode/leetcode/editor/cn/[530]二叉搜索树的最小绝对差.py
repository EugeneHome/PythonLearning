# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 
# 
#  差值是一个正数，其数值等于两值之差的绝对值。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [4,2,6,1,3]
# 输出：1
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是 [2, 10⁴] 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-
# nodes/ 相同 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 二叉树 👍 617 👎 0
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = list()
        inorder = list()
        cur = root
        min_diff = 100001
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            inorder.append(node.val)
            cur = node.right
            if len(inorder) > 1:
                min_diff = min(min_diff, abs(inorder[-1] - inorder[-2]))
                if min_diff == 1:
                    return min_diff
        return min_diff
    # leetcode submit region end(Prohibit modification and deletion)
