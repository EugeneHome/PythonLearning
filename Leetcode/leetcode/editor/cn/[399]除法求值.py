# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 
# values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。 
# 
#  另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj =
#  ? 的结果作为答案。 
# 
#  返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替
# 代这个答案。 
# 
#  注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。 
# 
#  注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"]
# ,["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
# 注意：x 是未定义的 => -1.0 
# 
#  示例 2： 
# 
#  
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]
#  
# 
#  示例 3： 
# 
#  
# 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],[
# "a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= equations.length <= 20 
#  equations[i].length == 2 
#  1 <= Ai.length, Bi.length <= 5 
#  values.length == equations.length 
#  0.0 < values[i] <= 20.0 
#  1 <= queries.length <= 20 
#  queries[i].length == 2 
#  1 <= Cj.length, Dj.length <= 5 
#  Ai, Bi, Cj, Dj 由小写英文字母与数字组成 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 数组 字符串 最短路 👍 1169 👎 0

from typing import List

"""
图+dfs
class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = dict() if neighbors is None else neighbors


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = dict()
        for [a, b], v in zip(equations, values):
            if a not in nodes:
                node = Node(a)
                nodes[a] = node
            if b not in nodes:
                node = Node(b)
                nodes[b] = node
            nodes[a].neighbors[b] = v
            nodes[b].neighbors[a] = 1.0 / v
        res = []
        for a, b in queries:
            if a not in nodes or b not in nodes:
                res.append(-1.0)
                continue
            if a == b:
                res.append(1.0)
            else:
                visited = set()
                stack = [nodes[a]]
                ratios = [1.0]
                tmp = -1.0
                while stack:
                    node = stack.pop()
                    ratio = ratios.pop()
                    if node in visited:
                        continue
                    if b in node.neighbors:
                        tmp = ratio * node.neighbors[b]
                        break
                    visited.add(node)
                    for n, v in node.neighbors.items():
                        stack.append(nodes[n])
                        ratios.append(ratio * v)
                res.append(tmp)
        return res
"""


# leetcode submit region begin(Prohibit modification and deletion)
# 并查集
class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.ratio = dict()
        self.rank = dict()

    def find(self, x):
        if x not in self.parent:
            return None, -1
        ratio = 1.0
        while self.parent[x] != x:
            ratio *= self.ratio[x]
            x = self.parent[x]
        return x, ratio

    def union(self, x, y, v):
        if x not in self.parent:
            self.parent[x] = x
            self.ratio[x] = 1.0
            self.rank[x] = 0
        if y not in self.parent:
            self.parent[y] = y
            self.ratio[y] = 1.0
            self.rank[y] = 0
        root_x, ratio_x = self.find(x)
        root_y, ratio_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.ratio[root_y] = ratio_x / ratio_y * v
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.ratio[root_x] = ratio_y / ratio_x / v
            else:
                self.parent[root_y] = root_x
                self.ratio[root_y] = ratio_x / ratio_y * v
                self.rank[root_x] += 1

    def get_ratio(self, x, y):
        root_x, ratio_x = self.find(x)
        root_y, ratio_y = self.find(y)
        if root_x is None or root_y is None or root_x != root_y:
            return -1.0
        return ratio_y / ratio_x


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for [a, b], v in zip(equations, values):
            uf.union(a, b, v)
        res = []
        for a, b in queries:
            res.append(uf.get_ratio(a, b))
        return res
# leetcode submit region end(Prohibit modification and deletion)
