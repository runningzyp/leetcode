#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (35.07%)
# Likes:    3317
# Dislikes: 0
# Total Accepted:    910.3K
# Total Submissions: 2.6M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
#
#
# 示例 1：
#
#
# 输入：x = 123
# 输出：321
#
#
# 示例 2：
#
#
# 输入：x = -123
# 输出：-321
#
#
# 示例 3：
#
#
# 输入：x = 120
# 输出：21
#
#
# 示例 4：
#
#
# 输入：x = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# -2^31
#
#
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        l1 = [x for x in str(x)]
        ret = 1
        if l1[0] == "-":
            ret = -1
            l1 = l1[1:]
        l1.reverse()
        result = "".join(l1)
        result = int(result.lstrip("0")) * ret
        if pow(-2, 31) < result < pow(2, 31) - 1:
            return result
        return 0


# @lc code=end
if __name__ == "__main__":
    assert Solution().reverse(0) == 0
