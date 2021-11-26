"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        a = []
        iter1 = self
        while iter1:
            a.append(iter1.val)
            iter1 = iter1.next
        return str(a)

    __repr__ = __str__


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = 0
        result = ListNode(val=0, next=None)
        iter1 = result
        while 1:
            val = (l1.val + l2.val + ret) % 10
            ret = (l1.val + l2.val + ret) // 10

            iter1.next = ListNode(val=val, next=None)
            iter1 = iter1.next
            l1 = l1.next or ListNode(val=0, next=None)
            l2 = l2.next or ListNode(val=0, next=None)
            if (
                l1.next is None
                and l2.next is None
                and l1.val == 0
                and l2.val == 0
                and not ret
            ):
                break
        return result.next


if __name__ == "__main__":

    a = [8, 3, 2]
    b = [9, 2, 1]
    a.reverse()
    b.reverse()
    l1 = None
    l2 = None
    for x in a:
        l1 = ListNode(val=x, next=l1)
    for x in b:
        l2 = ListNode(val=x, next=l2)
    print(Solution().addTwoNumbers(l1, l2))
    assert l == [8, 9, 0, 1]
