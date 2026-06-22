class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dicti = {}
        for char in text:
            dicti[char] = dicti.get(char, 0) + 1
        print(dicti)
        
        minVal = float('inf')
        for char in ['b','a','l','o','n']:
            divider = 1
            if char == 'l' or char == 'o':
                divider = 2
            
            howmany = dicti.get(char, 0) // divider
            minVal = min(minVal, howmany)
        
        return minVal

