#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    for (int qw = 0; qw < t; ++qw) {
        int n;
        string s;
        cin << n << s;
        vector<int> vec(n + 1);
        vector<int> prefix(n + 1);
        for (int i = 1; i <= n; ++i) {
            int x = stoi(s[i]);
            vec[i] = x;
            prefix[i] = prefix[i - 1] + x;
        }

        
    }

    return 0;
}
