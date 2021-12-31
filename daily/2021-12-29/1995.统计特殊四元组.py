#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#
# https://leetcode-cn.com/problems/count-special-quadruplets/description/
#
# algorithms
# Easy (56.35%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 28.4K
# Testcase Example:  '[1,2,3,6]'
#
# 给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：
#
#
# nums[a] + nums[b] + nums[c] == nums[d] ，且
# a < b < c < d
#
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,6]
# 输出：1
# 解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
#
#
# 示例 2：
#
# 输入：nums = [3,3,6,4,5]
# 输出：0
# 解释：[3,3,6,4,5] 中不存在满足要求的四元组。
#
#
# 示例 3：
#
# 输入：nums = [1,1,1,3,5]
# 输出：4
# 解释：满足要求的 4 个四元组如下：
# - (0, 1, 2, 3): 1 + 1 + 1 == 3
# - (0, 1, 3, 4): 1 + 1 + 3 == 5
# - (0, 2, 3, 4): 1 + 1 + 3 == 5
# - (1, 2, 3, 4): 1 + 1 + 3 == 5
#
#
#
#
# 提示：
#
#
# 4 <= nums.length <= 50
# 1 <= nums[i] <= 100
#
#
#

# @lc code=start
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for index, i in enumerate(nums[:-3]):
            for index1, j in enumerate(nums[index + 1 :]):
                for index2, m in enumerate(nums[index + index1 +2 :]):
                    for n in nums[index + index1 + index2 + 3 :]:
                        if i + j + m == n:
                            count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    assert Solution().countQuadruplets([1, 1, 1, 3, 5]) == 4
    assert Solution().countQuadruplets([3,3,6,4,5])==0
    assert Solution().countQuadruplets([9,6,8,23,39,23])==2
