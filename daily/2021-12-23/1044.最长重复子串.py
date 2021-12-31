#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#
# https://leetcode-cn.com/problems/longest-duplicate-substring/description/
#
# algorithms
# Hard (21.00%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 33.1K
# Testcase Example:  '"banana"'
#
# 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。
# 
# 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "banana"
# 输出："ana"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abcd"
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= s.length <= 3 * 10^4
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestDupSubstring(self, s: str) -> str:
# @lc code=end

