#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#
# https://leetcode-cn.com/problems/repeated-string-match/description/
#
# algorithms
# Medium (35.82%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    34.9K
# Total Submissions: 89.9K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
#
# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
#
#
#
# 示例 1：
#
# 输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
#
#
# 示例 2：
#
# 输入：a = "a", b = "aa"
# 输出：2
#
#
# 示例 3：
#
# 输入：a = "a", b = "a"
# 输出：1
#
#
# 示例 4：
#
# 输入：a = "abc", b = "wxyz"
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1 <= a.length <= 10^4
# 1 <= b.length <= 10^4
# a 和 b 由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        k = len(b)
        for i in range(k):
            if b in a * (i + 1):
                return i + 1
        return -1
        # if a == "aabaa" and b == "aaab":
        #     return 2
        # if b in a:
        #     return 1

        # count = 1
        # match = False
        # i = j = 0
        # index = 0
        # while j < len(b):
        #     if i == len(a):
        #         i = 0
        #         count += 1
        #     if count > 1 and a[i] != b[j]:
        #         return -1
        #     if count == 1 and a[i] != b[j] and match:
        #         j = 0
        #         index += 1
        #         i = index
        #         match = False
        #     elif count == 1 and a[i] != b[j] and not match:
        #         i += 1
        #         match = False
        #     elif a[i] == b[j]:
        #         i += 1
        #         j += 1
        #         match = True
        # # if set(b) != set(a) and count > 1:
        # #     return -1
        # return count


# @lc code=end
if __name__ == "__main__":
    assert Solution().repeatedStringMatch("abcd", "cdabcdab") == 3
    assert Solution().repeatedStringMatch("a", "aa") == 2
    assert Solution().repeatedStringMatch("a", "a") == 1
    assert Solution().repeatedStringMatch("abc", "wxyz") == -1
    assert Solution().repeatedStringMatch("abcd", "cdabcdab") == 3
    assert Solution().repeatedStringMatch("a", "aa") == 2
    assert Solution().repeatedStringMatch("a", "a") == 1
    assert Solution().repeatedStringMatch("abc", "wxyz") == -1
    assert Solution().repeatedStringMatch("abc", "abc") == 1
    assert Solution().repeatedStringMatch("abc", "cba") == -1
    assert Solution().repeatedStringMatch("abcabcabcabc", "abac") == -1
    assert Solution().repeatedStringMatch("aa", "a") == 1
    assert Solution().repeatedStringMatch("abab", "aba") == 1
    assert Solution().repeatedStringMatch("abaababa", "abaabaa") == 2
    assert Solution().repeatedStringMatch("gdeb", "ebg") == 2
