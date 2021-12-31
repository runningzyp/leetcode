#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#
# https://leetcode-cn.com/problems/perfect-number/description/
#
# algorithms
# Easy (41.85%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    47.4K
# Total Submissions: 101.9K
# Testcase Example:  '28'
#
# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
#
# 给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
#
#
#
# 示例 1：
#
#
# 输入：num = 28
# 输出：true
# 解释：28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, 和 14 是 28 的所有正因子。
#
# 示例 2：
#
#
# 输入：num = 6
# 输出：true
#
#
# 示例 3：
#
#
# 输入：num = 496
# 输出：true
#
#
# 示例 4：
#
#
# 输入：num = 8128
# 输出：true
#
#
# 示例 5：
#
#
# 输入：num = 2
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= num <= 10^8
#
#
#

# @lc code=start
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        l = []
        ret = 1
        while ret < math.sqrt(num):
            if num % ret == 0:
                l.append(ret)
                l.append(num//ret)
            ret += 1
        if num in l:
            l.remove(num)
        return num == sum(l)


# @lc code=end

if __name__ == "__main__":
    Solution().checkPerfectNumber(1) == True
