# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode|None, n: int) -> ListNode|None:
        """
        :param head: 链表头节点
        :param n: 要删除的倒数第n个节点
        :return: 删除后的链表头节点
        """
        len = 0
        cur = head

        while cur:
            len += 1
            cur = cur.next

        if len < n:
            return head
        if len == n:
            return head.next
        
        cur = head
        for i in range(len - n - 1):
            cur = cur.next
        
        cur.next = cur.next.next
        return head

    def removeNthFromEndPlus(self, head: ListNode|None, n: int) -> ListNode|None:
        """
        :param head: 链表头节点
        :param n: 要删除的倒数第n个节点
        :return: 删除后的链表头节点
        """
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
            if fast is None:       # n == 链表长度，要删头节点
                return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head





        

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    result = solution.removeNthFromEnd(head, n)
    print(result)


"""
================================================================================
题目：19. 删除链表的倒数第 N 个结点
================================================================================

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]
    解释：删除倒数第2个节点(4)，链表变为 [1,2,3,5]

示例 2：
    输入：head = [1], n = 1
    输出：[]

示例 3：
    输入：head = [1,2], n = 1
    输出：[1]

进阶：
    你能尝试使用一趟扫描实现吗？

================================================================================
"""


"""
================================================================================
算法思路
================================================================================

核心思想：
    先遍历一次链表得到长度 len，然后从头走 len-n-1 步找到待删除节点的前驱，
    通过修改前驱的 next 指针完成删除。

步骤：
    1. 第一趟遍历：从头走到尾，统计链表长度 len
    2. 边界情况处理：
       - 如果 len < n：返回 head（n 大于链表长度，无需删除）
       - 如果 len == n：删除的是头节点，直接返回 head.next
    3. 第二趟遍历：从头走 len-n-1 步，定位到待删除节点的前驱
    4. 通过 cur.next = cur.next.next 跳过待删除节点
    5. 返回 head

时间复杂度：O(n)
    虽然有两趟遍历，但每趟都是 O(n)，总体 O(n)

空间复杂度：O(1)
    只用了常数个变量

注：题目进阶要求"一趟扫描"，可以用快慢指针实现：
    - 快指针先走 n 步
    - 快慢指针同时走，当快指针到尾部时，慢指针正好在待删除节点的前驱
    - 这样只需一趟遍历

================================================================================
"""