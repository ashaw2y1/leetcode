1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman = {
4            'I' : 1,
5            'V' : 5,
6            'X' : 10,
7            'L' : 50,
8            'C' : 100,
9            'D' : 500,
10            'M' : 1000
11        }
12
13        total = 0
14        for i in range(len(s)-1):
15            if roman[s[i]] < roman[s[i+1]]:
16                total -= roman[s[i]]
17            else:
18                total += roman[s[i]]
19        
20        return total + roman[s[-1]]