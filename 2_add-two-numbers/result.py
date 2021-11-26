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


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        ret = len(num1) - len(num2)
        if ret < 0:
            ret *= -1
            num1.extend([0] * ret)
        elif ret > 0:
            num2.extend([0] * ret)
        ret = 0
        num3 = []
        for n1, n2 in zip(num1, num2):
            val = (n1 + n2 + ret) % 10
            num3.append(val)
            ret = (n1 + n2 + ret) // 10
        if ret != 0:
            num3.append(ret)
        result = None
        num3.reverse()
        for a in num3:
            result = ListNode(val=a, next=result)
        return result


if __name__ == "__main__":
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=9, next=None)))
    # l2 = ListNode(
    #     val=1,
    #     next=ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None))),
    # )
    l2 = ListNode(
        val=5,
        next=ListNode(val=6, next=ListNode(val=4, next=ListNode(val=9, next=None))),
    )
    result = Solution().addTwoNumbers(l1, l2)
    l = []
    while result:
        l.append(result.val)
        result = result.next
    assert l == [7, 0, 4, 0, 1]
