#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<pair<int, int>> A;
        for (int i = 0; i < n; i++) {
            int x, y; cin >> x >> y;
            A.push_back({x, y});
        }
        bool U = false, R = false, D = false, L = false;
        if (A.size() == 1) {
            cout << "YES" << endl;
        } else {
            for (int i = 1; i < A.size(); i++) {
                if (A[i].first > A[i - 1].first)
                    R = true;
                if (A[i].first < A[i - 1].first)
                    L = true;
                if (A[i].second > A[i - 1].second)
                    U = true;
                if (A[i].second < A[i - 1].second)
                    D = true;
            }
        }
        if (U == true && R == true && D == true && L == true)
            cout << "NO" << endl;
        else 
            cout << "YES" << endl;
    }
    return 0;
}