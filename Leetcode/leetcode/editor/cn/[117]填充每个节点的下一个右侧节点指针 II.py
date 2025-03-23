# 给定一个二叉树： 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指
# 针连接），'#' 表示每层的末尾。 
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 6000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。 
#  
# 
#  
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 链表 二叉树 👍 911 👎 0

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        """
        # 栈
        level_nodes = [root]
        while level_nodes:
            num = len(level_nodes)
            last = None
            for _ in range(num):
                node = level_nodes.pop(0)
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
                if last:
                    last.next = node
                last = node
        return root
        """
        # 链表
        cur=root
        while cur:
            next_head=Node()
            tmp=next_head
            while cur:
                if cur.left:
                    tmp.next=cur.left
                    tmp=tmp.next
                if cur.right:
                    tmp.next=cur.right
                    tmp=tmp.next
                cur=cur.next
            cur=next_head.next
        return root
# leetcode submit region end(Prohibit modification and deletion)
