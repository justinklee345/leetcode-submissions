class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0 for i in range(len(nums))]
        rightSum = [0 for i in range(len(nums))]

        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]

        answer = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            answer[i] = abs(leftSum[i] - rightSum[i])
        
        return answer
