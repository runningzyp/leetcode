from typing import List
from collections import Counter


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        l1 = [y for x in board for y in x]
        X_str = ""
        O_str = ""
        for index, v in enumerate(l1):
            if v == "X":
                X_str += str(index + 1)
            if v == "O":
                O_str += str(index + 1)
        count = Counter(l1)
        if (
            count.get("X", 0) != count.get("O", 0)
            and count.get("X", 0) != count.get("O", 0) + 1
        ):
            return False
        win_case = ["123", "456", "789", "147", "258", "369", "159", "1579", "357"]
        x_winer = 0
        o_winer = 0
        for case in win_case:
            if case in X_str:
                x_winer += 1
            if case in O_str:
                o_winer += 1
        if x_winer == o_winer == 1:
            return False
        if x_winer == 1 and count.get("X", 0) == count.get("O", 0):
            return False
        if o_winer == 1 and (count.get("X", 0) + count.get("O", 0)) == 9:
            return False
        return True


if __name__ == "__main__":
    assert Solution().validTicTacToe(["OXX", "XOX", "OXO"]) is False
