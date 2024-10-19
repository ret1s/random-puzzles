class Solution {
public:
    string reverseWords(string s) {
        stack<string> words;
        string tmp = "";
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ' ' && tmp != "") {
                words.push(tmp);
                tmp = "";
            }
            if (s[i] != ' ')
                tmp += s[i];
            if (i == s.length() - 1 && tmp != "")
                words.push(tmp);
        }

        string res = "";
        while (!words.empty()) {
            res += words.top();
            words.pop();
            if (words.size() >= 1)
                res += " ";
        }

        return res;
    }
};
// 16-08-2023
