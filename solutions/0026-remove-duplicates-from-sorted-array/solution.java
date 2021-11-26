class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int updatedIdx = 0;
        
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
            if (set.size() > updatedIdx) {
                nums[updatedIdx] = nums[i];
                updatedIdx++;
            }
        }
        return set.size();
    }
}
