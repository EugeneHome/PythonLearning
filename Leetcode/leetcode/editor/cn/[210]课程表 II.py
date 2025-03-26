# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 
# prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。 
# 
#  
#  例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。 
#  
# 
#  返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。 
# 
#  示例 3： 
# 
#  
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]
#  
# 
#  
# 提示：
# 
#  
#  1 <= numCourses <= 2000 
#  0 <= prerequisites.length <= numCourses * (numCourses - 1) 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  ai != bi 
#  所有[ai, bi] 互不相同 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 1017 👎 0

from typing import List

"""
# Kahn算法
class Node:
    def __init__(self, nexts=None):
        self.nexts = list() if nexts is None else nexts


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [Node() for _ in range(numCourses)]
        depends = [0] * numCourses
        for a, b in prerequisites:
            courses[b].nexts.append(a)
            depends[a] += 1
        finish = [i for i, d in enumerate(depends) if d == 0]
        result=finish.copy()
        while finish:
            new_finish = []
            for c in finish:
                for nc in courses[c].nexts:
                    depends[nc] -= 1
                    if depends[nc] == 0:
                        new_finish.append(nc)
            result.extend(new_finish)
            finish = new_finish
        return [] if len(result)!=numCourses else result
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, depends=None):
        self.depends = list() if depends is None else depends


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS
        courses = [Node() for _ in range(numCourses)]
        for a, b in prerequisites:
            courses[a].depends.append(b)
        visited = set()
        finish = list()
        cycle = False

        def dfs(x):
            nonlocal cycle
            visited.add(x)
            for c in courses[x].depends:
                if c not in visited:
                    dfs(c)
                    if cycle:
                        return
                elif c not in finish:
                    cycle = True
                    return
            finish.append(x)

        for i in range(numCourses):
            if cycle:
                return []
            if i not in visited:
                dfs(i)
        return finish
# leetcode submit region end(Prohibit modification and deletion)
