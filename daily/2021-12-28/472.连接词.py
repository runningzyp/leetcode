#
# @lc app=leetcode.cn id=472 lang=python3
#
# [472] 连接词
#
# https://leetcode-cn.com/problems/concatenated-words/description/
#
# algorithms
# Hard (39.10%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 26K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
# 
# 连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：words =
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
# 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
# ⁠    "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
# ⁠    "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
# 
# 
# 示例 2：
# 
# 
# 输入：words = ["cat","dog","catdog"]
# 输出：["catdog"]
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 10^4
# 0 <= words[i].length <= 1000
# words[i] 仅由小写字母组成
# 0 <= sum(words[i].length) <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
# @lc code=end

