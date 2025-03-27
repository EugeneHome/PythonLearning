# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = ""
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = "2"
# 输出：["a","b","c"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] 是范围 ['2', '9'] 的一个数字。 
#  
# 
#  Related Topics 哈希表 字符串 回溯 👍 3032 👎 0
from string import digits
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d2s = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = list(d2s[digits[0]])
        for i in range(1, len(digits)):
            s = d2s[digits[i]]
            tmp = list()
            for r in res:
                for c in s:
                    tmp.append(r + c)
            res = tmp
        return res
# leetcode submit region end(Prohibit modification and deletion)
