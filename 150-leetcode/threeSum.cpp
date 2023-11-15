class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        set<vector<int>> s;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0)
                break;
            int start = i + 1;
            int end = nums.size() - 1;
            while (start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                if (sum == 0) {
                    s.insert({nums[i], nums[start], nums[end]});
                    start++;
                    end--; 
                } else if (sum < 0)
                    start++;
                else if (sum > 0)
                    end--;
            }
        }
        for (auto a : s)
            res.push_back(a);
        return res;
    }
};