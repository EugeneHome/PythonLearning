# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。 
# 
#  完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层
# 为第 h 层（从第 0 层开始），则该层包含 1~ 2ʰ 个节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是[0, 5 * 10⁴] 
#  0 <= Node.val <= 5 * 10⁴ 
#  题目数据保证输入的树是 完全二叉树 
#  
# 
#  
# 
#  进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？ 
# 
#  Related Topics 位运算 树 二分查找 二叉树 👍 1230 👎 0
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 2
        left_length = 0
        right_length = 0
        cur = root
        while cur:
            left_length += 1
            cur = cur.left
        cur = root
        while cur:
            right_length += 1
            cur = cur.right
        if left_length == right_length:
            return 2 ** left_length - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
# leetcode submit region end(Prohibit modification and deletion)
