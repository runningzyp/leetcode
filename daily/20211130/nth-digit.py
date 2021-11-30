"""
400. 第 N 位数字
给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
 

提示：

1 <= n <= 231 - 1
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        #  通项公式 n(10)^(n-1)*9
        left = n
        lenth = 1
        while True:
            if left - pow(10, (lenth - 1)) * 9 * lenth > 0:
                left = left - pow(10, (lenth - 1)) * 9 * lenth
                lenth += 1
            else:
                break
        count = left // lenth
        ret = left % lenth
        number = pow(10, lenth - 1) - 1 + count
        if ret:
            return [int(x) for x in str(number + 1)][ret - 1]
        else:
            return [int(x) for x in str(number)][-1]


if __name__ == "__main__":
    s = Solution()
    assert s.findNthDigit(100) == 5
    assert s.findNthDigit(11) == 0
