"""
给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。

示例 1：

输入：s = "owoztneoer"
输出："012"
示例 2：

输入：s = "fviefuro"
输出："45"
 

提示：

1 <= s.length <= 105
s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一
s 保证是一个符合题目要求的字符串


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-original-digits-from-english
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter, defaultdict


# class Solution(object):
    # def originalDigits(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     strings = [x for x in s]
    #     orders = defaultdict(int)
    #     maps = {
    #         "0": ["z", "e", "r", "o"],
    #         "1": ["o", "n", "e"],
    #         "2": ["t", "w", "o"],
    #         "3": ["t", "h", "r", "e", "e"],
    #         "4": ["f", "o", "u", "r"],
    #         "5": ["f", "i", "v", "e"],
    #         "6": ["s", "i", "x"],
    #         "7": ["s", "e", "v", "e", "n"],
    #         "8": ["e", "i", "g", "h", "t"],
    #         "9": ["n", "i", "n", "e"],
    #     }

    #     count = {
    #         "z": 1,
    #         "e": 9,
    #         "r": 3,
    #         "o": 4,
    #         "n": 4,
    #         "t": 3,
    #         "w": 1,
    #         "h": 2,
    #         "f": 2,
    #         "u": 1,
    #         "i": 4,
    #         "v": 2,
    #         "s": 2,
    #         "x": 1,
    #         "g": 1,
    #     }

    #     while "z" in strings:
    #         strings.remove("z")
    #         strings.remove("e")
    #         strings.remove("r")
    #         strings.remove("o")
    #         orders[0] += 1
    #     while "w" in strings:
    #         strings.remove("t")
    #         strings.remove("w")
    #         strings.remove("o")
    #         orders[2] += 1
    #     while "u" in strings:
    #         strings.remove("f")
    #         strings.remove("o")
    #         strings.remove("u")
    #         strings.remove("r")
    #         orders[4] += 1
    #     while "x" in strings:
    #         strings.remove("s")
    #         strings.remove("i")
    #         strings.remove("x")
    #         orders[6] += 1
    #     while "g" in strings:
    #         strings.remove("e")
    #         strings.remove("i")
    #         strings.remove("g")
    #         strings.remove("h")
    #         strings.remove("t")
    #         orders[8] += 1
    #     while "h" in strings:
    #         strings.remove("t")
    #         strings.remove("h")
    #         strings.remove("r")
    #         strings.remove("e")
    #         strings.remove("e")
    #         orders[3] += 1
    #     while "s" in strings:
    #         strings.remove("s")
    #         strings.remove("e")
    #         strings.remove("v")
    #         strings.remove("e")
    #         strings.remove("n")
    #         orders[7] += 1
    #     while "v" in strings:
    #         strings.remove("f")
    #         strings.remove("i")
    #         strings.remove("v")
    #         strings.remove("e")
    #         orders[5] += 1
    #     while "o" in strings:
    #         strings.remove("o")
    #         strings.remove("n")
    #         strings.remove("e")
    #         orders[1] += 1
    #     orders[9] = len(strings) / 4
    #     return "".join(str(x) * orders[x] for x in range(10))



class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        maps = {k: 0 for k in range(10)}
        maps[0] = count["z"]
        maps[2] = count["w"]
        maps[4] = count["u"]
        maps[6] = count["x"]
        maps[8] = count["g"]
        maps[3] = count["h"] - maps[8]
        maps[7] = count["s"] - maps[6]
        maps[5] = count["f"] - maps[4]
        maps[1] = count["o"] - maps[0] - maps[2] - maps[4]
        maps[9] = count["i"] - maps[5] - maps[6] - maps[8]
        return "".join(str(x) * maps[x] for x in range(10))

if __name__ == "__main__":
    s = """"""
    print(Solution().originalDigits(s))
