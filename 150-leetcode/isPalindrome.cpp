class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> t;
        for (const auto& c : s) {
            if (c >= 'A' && c <= 'Z')
                t.push_back(c - 'A' + 'a');
            else if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9'))
                t.push_back(c);
        }

        int size = t.size();
        for (int i = 0; i < size/2; i++) 
            if (t[i] != t[size - i - 1])
                return false;
        
        return true;
    }
};