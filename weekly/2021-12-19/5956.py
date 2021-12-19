from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


if __name__ == "__main__":
    s = Solution()
    assert s.firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"]) == "ada"
