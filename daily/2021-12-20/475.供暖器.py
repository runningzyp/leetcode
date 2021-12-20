#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Medium (33.95%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    41.3K
# Total Submissions: 106.6K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
#
# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
#
# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#
#
# 示例 1:
#
#
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#
#
# 示例 2:
#
#
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#
#
# 示例 3：
#
#
# 输入：houses = [1,5], heaters = [2]
# 输出：3
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start
from typing import List
from collections import OrderedDict


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        subquence = OrderedDict()
        result = 0
        total = list(set(houses + heaters))
        total.sort()
        length = len(total)
        for index, v in enumerate(total):
            if v in heaters:
                subquence[index] = (True, v)
            else:
                subquence[index] = (False, v)
        heatersIndex = [k for k, v in subquence.items() if v[0]]
        first_index = heatersIndex[0]
        try:
            second_index = heatersIndex[heatersIndex.index(first_index) + 1]
        except Exception:
            second_index = first_index
        for index, v in subquence.items():
            if v[0]:
                first_index = index
                try:
                    second_index = heatersIndex[heatersIndex.index(first_index) + 1]
                except Exception:
                    second_index = first_index
                continue
            else:
                innerMin = min(
                    abs(v[1] - total[first_index]),
                    abs(total[second_index] - v[1]),
                )
            result = max(result, innerMin)
            if index > second_index:
                second_index = first_index
        return result


# @lc code=end

if __name__ == "__main__":
    assert Solution().findRadius([1, 5], [10]) == 9
