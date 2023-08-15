class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int size = candies.size();
        vector<bool> res(size, false);
        int cmax = 0;
        for (int i = 0; i < size; i++)
            if (candies[i] >= cmax)
                cmax = candies[i];
        for (int i = 0; i < size; i++)
            if (candies[i] + extraCandies >= cmax)
                res[i] = true;
        return res;
    }
};
