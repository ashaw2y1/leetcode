1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        strs.sort()
4
5        minLength = min(len(strs[0]), len(strs[-1]))
6
7        i = 0
8        while i < minLength and strs[0][i] == strs[-1][i]:
9            i += 1
10
11        return strs[0][:i]