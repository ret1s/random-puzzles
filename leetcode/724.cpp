class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int size = nums.size(), total = 0;
        for (int i = 0; i < size; i++)
            total += nums[i];
        int left = 0, right = total - nums[0];
        if (left == right)
            return 0; 
        for (int i = 1; i < size; i++) {
            left += nums[i - 1];
            right -= nums[i];
            if (left == right)
                return i;
        }  
        return -1;
    }
};
