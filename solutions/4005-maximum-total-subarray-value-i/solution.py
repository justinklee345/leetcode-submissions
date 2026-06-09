class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minVal = min(nums)
        maxVal = max(nums)
        return (maxVal - minVal) * k

        
