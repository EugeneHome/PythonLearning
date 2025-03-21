# 给你一个链表的头节点 head ，判断链表中是否有环。 
# 
#  如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到
# 链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。 
# 
#  如果链表中存在环 ，则返回 true 。 否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围是 [0, 10⁴] 
#  -10⁵ <= Node.val <= 10⁵ 
#  pos 为 -1 或者链表中的一个 有效索引 。 
#  
# 
#  
# 
#  进阶：你能用 O(1)（即，常量）内存解决此问题吗？ 
# 
#  Related Topics 哈希表 链表 双指针 👍 2297 👎 0
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 哈希表
        """
        ht = set()
        while head:
            if head in ht:
                return True
            ht.add(head)
            head = head.next
        return False
        """
        # 快慢指针
        if head is None or head.next is None:
            return False
        quick = head.next
        slow = head
        while quick != slow:
            if quick is None or quick.next is None:
                return False
            quick = quick.next.next
            slow = slow.next
        return True
# leetcode submit region end(Prohibit modification and deletion)
