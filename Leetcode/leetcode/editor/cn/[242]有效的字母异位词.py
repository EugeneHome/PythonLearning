# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
# 
#  Related Topics 哈希表 字符串 排序 👍 993 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = dict()
        hasht=dict()
        for st,ha in zip([s,t],[hashs,hasht]):
            for c in st:
                if c in ha:
                    ha[c] += 1
                else:
                    ha[c] = 1
        return hashs==hasht
# leetcode submit region end(Prohibit modification and deletion)
