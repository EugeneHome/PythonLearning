# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。 
# 
#  你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#  
# 
#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 
# 
#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。 
# 
#  注意: 
# 
#  
#  单词是指由非空格字符组成的字符序列。 
#  每个单词的长度大于 0，小于等于 maxWidth。 
#  输入单词数组 words 至少包含一个单词。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: words = ["This", "is", "an", "example", "of", "text", "justification."], 
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#  
# 
#  示例 2: 
# 
#  
# 输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。       
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#  
# 
#  示例 3: 
# 
#  
# 输入:words = ["Science","is","what","we","understand","well","enough","to",
# "explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 2
# 0
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= words.length <= 300 
#  1 <= words[i].length <= 20 
#  words[i] 由小写英文字母和符号组成 
#  1 <= maxWidth <= 100 
#  words[i].length <= maxWidth 
#  
# 
#  Related Topics 数组 字符串 模拟 👍 462 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = [[words[0]]]
        cur_l = len(words[0])
        for i in range(1,len(words)):
            l = len(words[i])
            if cur_l + 1 + l <= maxWidth:
                ans[-1].append(words[i])
                cur_l = cur_l + 1 + l
            else:
                ans[-1] = self.trans(ans[-1], maxWidth - cur_l)
                ans.append([words[i]])
                cur_l = l
        ans[-1] = " ".join(ans[-1]) + " " * (maxWidth - cur_l)
        return ans

    def trans(self, word_list, space_num):
        n = len(word_list) - 1
        if n == 0:
            return word_list[0] + " " * space_num
        s = ""
        add_space = space_num // n + 1
        extra_space = space_num % n
        for i in range(n):
            s = s + word_list[i] + " " * add_space
            if i < extra_space:
                s = s + " "
        return s + word_list[n]

# leetcode submit region end(Prohibit modification and deletion)
