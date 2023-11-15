class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            int a = target - nums[i];
            if (m.count(a))
                return {m[a], i};
            m[nums[i]] = i;
        }
        return {};
    }
};