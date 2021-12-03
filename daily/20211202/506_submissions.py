"""
给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。

运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：

名次第 1 的运动员获金牌 "Gold Medal" 。
名次第 2 的运动员获银牌 "Silver Medal" 。
名次第 3 的运动员获铜牌 "Bronze Medal" 。
从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。

 

示例 1：

输入：score = [5,4,3,2,1]
输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"]
解释：名次为 [1st, 2nd, 3rd, 4th, 5th] 。
示例 2：

输入：score = [10,3,8,9,4]
输出：["Gold Medal","5","Bronze Medal","Silver Medal","4"]
解释：名次为 [1st, 5th, 3rd, 2nd, 4th] 。
 

提示：

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
score 中的所有值 互不相同


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-ranks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import *
from collections import defaultdict
import copy


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = defaultdict(str)
        score_b = copy.deepcopy(score)
        score.sort(reverse=True)
        for index, data in enumerate(score):
            d[data] = index + 1
        maps = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        return [str(maps.get(d[data]) or d[data]) for data in score_b]


if __name__ == "__main__":
    s = Solution()
    assert s.findRelativeRanks([10, 3, 8, 9, 4]) == [
        "Gold Medal",
        "5",
        "Bronze Medal",
        "Silver Medal",
        "4",
    ]
