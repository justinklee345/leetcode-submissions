class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        retVal = ""
        for word in words:
            weight = 0
            for letter in word:
                weight += weights[ord(letter) - ord('a')]
            
            retVal += chr(ord('z') - weight % 26)
        
        return retVal
