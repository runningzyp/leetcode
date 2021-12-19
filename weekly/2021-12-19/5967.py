from typing import List
from collections import OrderedDict


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        d = OrderedDict()
        for index, val in enumerate(s):
            d.update({index: val})
        for space in spaces:
            d[space] = " " + d[space]
        return "".join(d.values())


if __name__ == "__main__":
    assert (
        Solution().addSpaces(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6])
        == " s p a c i n g"
    )
