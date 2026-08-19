from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        :param headA: 链表A的头节点
        :param headB: 链表B的头节点
        :return: 相交节点
        """
        p = headA
        q = headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        
        return p

if __name__ == "__main__":
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next

    solution = Solution()
    if solution.getIntersectionNode(headA, headB):
        print("Intersected at", "'",solution.getIntersectionNode(headA, headB).val,"'")
    else:
        print("No intersection")


"""
================================================================================
题目：160. 相交链表
================================================================================

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
如果两个链表不存在相交节点，返回 null 。

图示两个链表在节点 c1 开始相交：

    A:  a1 → a2 ──┐
                   └→ c1 → c2 → c3
    B:  b1 → b2 → b3 ──┘

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须保持其原始结构。

示例 1：
    输入：intersectVal = 8, listA = [4,1,8,4,5], skipA = 2, skipB = 3
    输出：Intersected at '8'
    解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。

示例 2：
    输入：intersectVal = 2, listA = [1,9,1,2,4], skipA = 3, skipB = 2
    输出：Intersected at '2'

示例 3：
    输入：intersectVal = 0, listA = [2,6,4], skipA = 3, skipB = 1
    输出：No intersection
    解释：两个链表不相交，返回 null。

进阶：
    你能否设计一个时间复杂度 O(m + n)、空间复杂度 O(1) 的解决方案？

================================================================================
"""


"""
================================================================================
算法思路
================================================================================

核心思想：
    使用双指针（交叉指针法），两个指针分别从 A 和 B 头部出发，
    遍历完各自链表后切换到另一个链表继续遍历。
    这样两个指针走过的总路径长度相同，最终会在相交点相遇。

步骤：
    1. 初始化指针 p = headA, q = headB
    2. 当 p != q 时循环：
       a. 如果 p 不为空：p = p.next
          如果 p 为空：p = headB（切换到 B 链表继续走）
       b. 如果 q 不为空：q = q.next
          如果 q 为空：q = headA（切换到 A 链表继续走）
    3. 循环结束时，p == q：
       - 如果相交：p/q 就是相交节点
       - 如果不相交：p/q 都是 None，返回 None

为什么这样可行？
    - 假设 A 链表长度为 a + c，B 链表长度为 b + c
      （c 为相交后的公共部分长度）
    - p 走过的路径：A + B = a + c + b + c
    - q 走过的路径：B + A = b + c + a + c
    - 两者总长度相同 = a + b + 2c
    - 前 a + b 步，p 和 q 一定不同
    - 第 a + b + 1 步开始，p 和 q 同时进入公共部分 c，相遇！
    - 如果不相交（c = 0），两人都走了 a + b 步后同时为 None

示例：A=[4,1,8,4,5], B=[5,6,1,8,4,5]
    p: 4→1→8→4→5 → 5→6→1→8→4→5 → (相遇在8)
    q: 5→6→1→8→4→5 → 4→1→8→4→5 → (相遇在8)

时间复杂度：O(m + n)
    m、n 分别为两个链表的长度，每个指针最多遍历 m+n 次

空间复杂度：O(1)
    只用了两个指针变量

================================================================================
"""