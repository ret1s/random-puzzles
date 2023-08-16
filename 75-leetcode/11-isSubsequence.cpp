class Solution {
public:
    bool isSubsequence(string s, string t) {
        int j = 0;
        for (int i = 0; i < t.length(); i++) {
            if (s[j] == t[i])
                j++;
            if (j == s.length())
                return true;
        }
        return j == s.length();
    }
};
// 16-08-2023
