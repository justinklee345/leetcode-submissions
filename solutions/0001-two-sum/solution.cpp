class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        for (int idx = 0; idx < nums.size(); idx++) {
            int curr_val = nums.at(idx);
            if (map.find(target - curr_val) != map.end()) {
                return vector<int>{map.find(target - curr_val)->second, idx};
            } else {
                map.insert({curr_val, idx});
            }
        }
        return vector<int>{-1, -1};
    }
};
