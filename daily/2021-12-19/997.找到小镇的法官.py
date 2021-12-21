#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#
# https://leetcode-cn.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (51.06%)
# Likes:    211
# Dislikes: 0
# Total Accepted:    55.5K
# Total Submissions: 104.2K
# Testcase Example:  '2\n[[1,2]]'
#
# 在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。
#
# 如果小镇的法官真的存在，那么：
#
#
# 小镇的法官不相信任何人。
# 每个人（除了小镇法官外）都信任小镇的法官。
# 只有一个人同时满足条件 1 和条件 2 。
#
#
# 给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。
#
# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。
#
#
#
# 示例 1：
#
#
# 输入：n = 2, trust = [[1,2]]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：n = 3, trust = [[1,3],[2,3]]
# 输出：3
#
#
# 示例 3：
#
#
# 输入：n = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1
#
#
# 示例 4：
#
#
# 输入：n = 3, trust = [[1,2],[2,3]]
# 输出：-1
#
#
# 示例 5：
#
#
# 输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 输出：3
#
#
#
# 提示：
#
#
# 1
# 0
# trust[i].length == 2
# trust[i] 互不相同
# trust[i][0] != trust[i][1]
# 1
#
#
#
# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1 if n == 1 else -1
        l1 = list(zip(*trust))[1]
        l0 = list(zip(*trust))[0]
        count = Counter(l1)
        for k, v in count.items():
            if v != n - 1:
                continue
            if k not in l0:
                return k
        return -1


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
    assert s.findJudge(3, [[1, 2], [2, 3]]) == -1
