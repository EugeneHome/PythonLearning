# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  m == s.length 
#  n == t.length 
#  1 <= m, n <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 
# o(m+n) 时间内解决此问题的算法吗？
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 3191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_hash=dict()
        for c in t:
            if c in t_hash:
                t_hash[c]+=1
            else:
                t_hash[c]=1
        left=0
        win_hash=dict()
        win_min=""
        t_remain=len(t)
        for i,c in enumerate(s):
            if c not in t_hash:
                continue
            if c in win_hash:
                win_hash[c]+=1
            else:
                win_hash[c]=1
            if win_hash[c]<=t_hash[c]:
                t_remain-=1
            while t_remain==0:
                if s[left] in win_hash:
                    if win_min=="" or (i+1-left)<len(win_min):
                        win_min=s[left:i+1]
                    win_hash[s[left]] -= 1
                    if win_hash[s[left]]<t_hash[s[left]]:
                        t_remain=1
                left+=1
        return win_min
# leetcode submit region end(Prohibit modification and deletion)