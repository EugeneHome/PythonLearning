# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 
#  
#  
#  每条从根节点到叶节点的路径都代表一个数字： 
#  
#  
# 
#  
#  例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。 
#  
# 
#  计算从根节点到叶节点生成的 所有数字之和 。 
# 
#  叶节点 是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3]
# 输出：25
# 解释：
# 从根到叶子节点路径 1->2 代表数字 12
# 从根到叶子节点路径 1->3 代表数字 13
# 因此，数字总和 = 12 + 13 = 25 
# 
#  示例 2： 
#  
#  
# 输入：root = [4,9,0,5,1]
# 输出：1026
# 解释：
# 从根到叶子节点路径 4->9->5 代表数字 495
# 从根到叶子节点路径 4->9->1 代表数字 491
# 从根到叶子节点路径 4->0 代表数字 40
# 因此，数字总和 = 495 + 491 + 40 = 1026
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 1000] 内 
#  0 <= Node.val <= 9 
#  树的深度不超过 10 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 801 👎 0
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        level_nodes = [root]
        level_nums = [root.val]
        res = 0
        while level_nodes:
            n = len(level_nodes)
            for _ in range(n):
                node = level_nodes.pop(0)
                num = level_nums.pop(0)
                if not node.left and not node.right:
                    res = res + num
                if node.left:
                    level_nodes.append(node.left)
                    level_nums.append(num * 10 + node.left.val)
                if node.right:
                    level_nodes.append(node.right)
                    level_nums.append(num * 10 + node.right.val)
        return res
# leetcode submit region end(Prohibit modification and deletion)
