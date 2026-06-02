class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        best = float("inf")
        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                if landStartTime[j] >= waterStartTime[i] + waterDuration[i]:
                    best = min(best, landStartTime[j] + landDuration[j])
                else:
                    best = min(best, waterStartTime[i] + waterDuration[i] + landDuration[j])

        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                if waterStartTime[j] >= landStartTime[i] + landDuration[i]:
                    best = min(best, waterStartTime[j] + waterDuration[j])
                else:
                    best = min(best, landStartTime[i] + landDuration[i] + waterDuration[j])
        
        return best
