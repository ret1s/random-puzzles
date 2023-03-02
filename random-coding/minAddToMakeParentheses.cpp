string reverseWord(string s, int n) {
    if (n == -1)
        return "";
    return s[n] + reverseWord(s, n - 1);
}

string helper(string s, string str, string tmp, int n) {
    if (n == -1)
        return str;
    if (s[n] == ' ') {
        tmp = reverseWord(tmp, tmp.length() - 1);
        str += tmp;
        str += ' ';
        tmp = "";
    }
    else if (n == 0) {
        tmp += s[n];
        tmp = reverseWord(tmp, tmp.length() - 1);
        str += tmp;
    }
    else
        tmp += s[n];
    return helper(s, str, tmp, n - 1);
}

string reverseSentence(string s) {
    int size = s.length();
    string str = "", tmp = "", res = "";
    res = helper(s, str, tmp, size - 1);
    
    return res;
}
