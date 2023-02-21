class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int res;
        if (nums.size() == 1)
            return nums[0];
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i + 1] == nums[i]) {
                ++i;
            }
            else {
                res = nums[i];
                break;
            }
        } 
        return res;
    }
};
