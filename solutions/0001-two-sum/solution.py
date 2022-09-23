class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through the list and create a dictionary that maps the value to a tuple of its idx and the target - the key value
        targetMap = {}
        for idx, val in enumerate(nums):
            if (targetMap.get(target - val, -1) != -1):
                return [targetMap.get(target - val), idx]
            targetMap.setdefault(val, idx)
            
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i, j]
        # return [-1, -1]
        
        
            
        
        
