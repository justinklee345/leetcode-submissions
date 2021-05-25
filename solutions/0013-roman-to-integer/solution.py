class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        integer = 0

        for digit in range(0, len(s)):
            if digit == len(s) - 1:
                integer += roman[s[digit]]
            else:
                if roman[s[digit]] < roman[s[digit+1]]:
                    integer -= roman[s[digit]]
                else:
                    integer += roman[s[digit]]
        
        return integer
