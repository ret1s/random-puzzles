class Solution {
public:
    int partitionString(string s) {
        int count = 0, size = s.length();
        bool check = false;
        vector<int> a(26, 0);
        for (int i = 0; i < size; i++) {
            int index = (int) s[i] - 'a';
            if (a[index] > 0) {
                if (i == size - 1) {
                    count += 2;
                }
                else {
                    count++;
                    for (int j = 0; j < 26; j++) 
                        a[j] = 0;
                    a[index]++;
                }
            } 
            else {
                if (i == size - 1)
                    count++;
                else   
                    a[index]++;
            }
        }    
        return count; 
    }
};
