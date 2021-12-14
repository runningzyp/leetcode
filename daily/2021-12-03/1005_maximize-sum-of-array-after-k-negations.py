"""
给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：

选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
重复这个过程恰好 k 次。可以多次选择同一个下标 i 。

以这种方式修改数组后，返回数组 可能的最大和 。

 

示例 1：

输入：nums = [4,2,3], k = 1
输出：5
解释：选择下标 1 ，nums 变为 [4,-2,3] 。
示例 2：

输入：nums = [3,-1,0,2], k = 3
输出：6
解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
示例 3：

输入：nums = [2,-3,-1,5,-4], k = 2
输出：13
解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
 

提示：

1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import *


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        negativeNums = [x for x in nums if x < 0]
        positiveNums = [x for x in nums if x >= 0]

        negativeNums.sort()
        if k <= len(negativeNums):
            negativeNums = [
                abs(x) if index < k else x for index, x in enumerate(negativeNums)
            ]
            return sum(negativeNums + positiveNums)
        if k > len(negativeNums):
            negativeNums = [abs(x) for x in negativeNums]
            ret = k - len(negativeNums)
            positiveNums.extend(negativeNums)
            positiveNums.sort()
            if ret % 2 == 0:
                return sum(positiveNums)
            else:
                positiveNums[0] = positiveNums[0] * -1
                return sum(positiveNums)


if __name__ == "__main__":
    assert Solution().largestSumAfterKNegations([3, -1, 0, 2], 3) == 6
    assert Solution().largestSumAfterKNegations([2, -3, -1, 5, -4], 2) == 13
