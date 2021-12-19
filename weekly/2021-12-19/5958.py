from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        count = 1
        yesterday = None
        for price in prices:
            if yesterday is None:
                yesterday = price
                continue
            if price != yesterday - 1:

                result += count * (count + 1) / 2
                count = 1
            else:
                count += 1
            yesterday = price
        result = int(result) + int(count * (count + 1) / 2)
        return result


if __name__ == "__main__":
    assert Solution().getDescentPeriods([1]) == 1
