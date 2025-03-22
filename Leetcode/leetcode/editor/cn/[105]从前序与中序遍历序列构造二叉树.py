# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并
# 返回其根节点。 
# 
#  
# 
#  示例 1: 
#  
#  
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder 和 inorder 均 无重复 元素 
#  inorder 均出现在 preorder 
#  preorder 保证 为二叉树的前序遍历序列 
#  inorder 保证 为二叉树的中序遍历序列 
#  
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 2500 👎 0
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root = TreeNode(val=preorder[pre_left])
            index = ht[root.val]
            ltree = index - in_left
            root.left = build(pre_left + 1, pre_left + ltree, in_left, index - 1)
            root.right = build(pre_left + 1 + ltree, pre_right, index + 1, in_right)
            return root

        ht = {v: i for i, v in enumerate(inorder)}
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)

# leetcode submit region end(Prohibit modification and deletion)
