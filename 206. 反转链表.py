# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode|None) -> ListNode|None:
        """
        :param head: 链表头节点
        :return: 反转后的链表头节点
        """
        if head is None:
            return head
        
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverseList(head)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    print(vals)


"""
================================================================================
题目：206. 反转链表
================================================================================

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

示例 2：
    输入：head = [1,2]
    输出：[2,1]

示例 3：
    输入：head = []
    输出：[]

================================================================================
"""


"""
================================================================================
算法思路
================================================================================

核心思想：
    使用迭代法，逐个节点翻转指针方向。
    每一步将当前节点的 next 指针指向前一个节点。

步骤：
    1. 初始化 prev = None, cur = head
    2. 遍历链表：
       a. 保存 cur.next 到 next（防止断链）
       b. 将 cur.next 指向 prev（翻转指针）
       c. prev = cur（prev 前移）
       d. cur = next（cur 前移）
    3. 循环结束后 prev 就是新的头节点

时间复杂度：O(n)
    只需遍历链表一次

空间复杂度：O(1)
    只用了常数个变量

================================================================================
"""