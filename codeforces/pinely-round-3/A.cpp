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
        set<pair<int, int>> T(A.begin(), A.end());
        A.assign(T.begin(), T.end());
        int U = 0, R = 0, D = 0, L = 0;
        if (A[0].first > 0) R = 1;
        else 1;
        if (A[0].second > 0) U = 1;
        else D = 1;
        for (int i = 0; i < n - 1; i++) {
            int X1 = A[i].first, X2 = A[i + 1].first, Y1 = A[i].second, Y2 = A[i + 1].second;
            if (Y2 > Y1) U = 1;
            else D = 1;
            
            if (X2 > X1) R = 1;
            else L = 1;
        }
        if (U + R + D + L == 4)
            cout << "NO" << endl;
        else 
            cout << "YES" << endl;
    }
    return 0;
}