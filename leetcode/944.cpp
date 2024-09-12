class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int size = strs.size();
        int a = 0;
        if (size != 0)
            a = strs[0].length();

        int res = 0;
        for (int col = 0; col < a; col++) {
            for (int row = 0; row < size - 1; row++) {
                if (strs[row][col] > strs[row + 1][col]) {
                  res += 1;
                  break;  
                }
            }
        }

        return res;
    }
};