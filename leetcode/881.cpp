class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end(), greater<int>());
        int res = 0;
        int i = 0, j = people.size() - 1;
        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                res++;
                i++;
                j--;
            }
            else {
                res++;
                i++;
            }
        }
        return res;
    }
};
