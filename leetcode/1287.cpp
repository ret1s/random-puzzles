class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int size = arr.size();
        unordered_map<int, int> m;
        for (int i : arr)
            m[i]++;
        for (const auto& a : m)
            if (a.second > size / 4)
                return a.first;
        
        return -1;
    }
};