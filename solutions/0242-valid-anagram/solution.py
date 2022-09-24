class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        for charac in s:
            sDict.setdefault(charac, 0)
            sDict[charac] += 1
        tDict = {}
        for charac in t:
            tDict.setdefault(charac, 0)
            tDict[charac] += 1
#         for k, v in sDict.items():
#             if (tDict.get(k) != v):
#                 return False
            
#         for k, v in tDict.items():
#             if (sDict.get(k) != v):
#                 return False
        return sDict == tDict
