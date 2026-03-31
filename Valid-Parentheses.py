1class Solution:
2    def isValid(self, s: str) -> bool:
3        while "()" in s or "{}" in s or "[]" in s:
4            s = s.replace("()", "").replace("{}", "").replace("[]", "")
5        
6        return s == ""