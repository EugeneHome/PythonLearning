# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# 如果 needle 不是 haystack 的一部分，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack 和 needle 仅由小写英文字符组成 
#  
# 
#  Related Topics 双指针 字符串 字符串匹配 👍 2381 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP，计算needle每个位置的相同前后缀长度pi
        # 匹配haystack和needle，如果匹配不上，跳到pi前一个位置对应的needle位置
        # 因为needle前一个位置的后缀部分已经和haystack比较一致了，此时将needle跳到前缀部分，可以保障仍一致
        # 循环pi直至needle的当前字符能和haystack匹配上，或者回到needle的首字符
        pi = [0]
        j=0
        for i in range(1, len(needle)):
            while j>0 and needle[i] != needle[j]:
                j=pi[j-1]
            if needle[i]==needle[j]:
                j=j+1
            pi.append(j)
        i, j = 0, 0
        while j < len(needle) and i < len(haystack):
            if haystack[i] == needle[j]:
                j = j + 1
            else:
                while j > 0:
                    j = pi[j - 1]
                    if haystack[i] == needle[j]:
                        j = j + 1
                        break
                else:
                    j = 0
            i = i + 1
        if j == len(needle):
            return i - j
        else:
            return -1
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.strStr("ababcaababcaabc", "ababcaabc"))
