#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n=0
        g.sort()  #孩子
        s.sort()  #饼干
        for i in s:
            for j in g:
                if(i>=j):
                    n+=1
                    del g[g.index(g[j],0)]
                    del s[s.index(s[j],0)]
        return n
# @lc code=end