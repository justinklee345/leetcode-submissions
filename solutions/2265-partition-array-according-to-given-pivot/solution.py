class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        below = []
        equal = []
        above = []

        for i in nums:
            if i < pivot:
                below.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                above.append(i)
        
        return below + equal + above
