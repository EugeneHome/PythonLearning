# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并
# 返回这颗 二叉树 。 
# 
#  
# 
#  示例 1: 
#  
#  
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder 和 postorder 都由 不同 的值组成 
#  postorder 中每一个值都在 inorder 中 
#  inorder 保证是树的中序遍历 
#  postorder 保证是树的后序遍历 
#  
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 1318 👎 0
from typing import List, Optional


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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(post_left, post_right, in_left, in_right):
            if post_left > post_right:
                return None
            root = TreeNode(val=postorder[post_right])
            index = ht[root.val]
            ltree = index - in_left
            root.left = build(post_left, post_left + ltree - 1, in_left, index - 1)
            root.right = build(post_left + ltree, post_right - 1, index + 1, in_right)
            return root

        ht = {v: i for i, v in enumerate(inorder)}
        n = len(inorder)
        return build(0, n - 1, 0, n - 1)
# leetcode submit region end(Prohibit modification and deletion)
