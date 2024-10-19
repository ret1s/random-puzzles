class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> m;
        for (char c : magazine) {
            if (m.count(c) == 0)
                m[c] = 1;
            else 
                m[c]++;
        }
        for (char c : ransomNote) {
            if (m[c] > 0)
                m[c]--;
            else
                return false;
        }
        return true;
    }
};