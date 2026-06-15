#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    
    int n;
    cin >> n;

    vector<pair<bool, int>> v(n);
    char c;
    pair<bool, int> p = {false, 0};

    for (int i = 0; i < n; i++) {
        cin >> c >> p.second;
        if (c == 'L') { p.first = false; }
        else if (c == 'G') { p.first = true; }
        v[i] = p;
    }

    sort(v.begin(), v.end(), [](const pair<bool,int>& a, const pair<bool,int>& b) { return a.second < b.second; });

    int max_lie{};

    for (pair<bool, int> out : v) {
        int i = out.second;
        int num_lie{};
        for (pair<bool, int> in : v) {
            if ((!in.first && in.second > i) || (in.first && in.second < i)) {
                num_lie++;
            }
        }
        if (num_lie > max_lie) { max_lie = num_lie; }
    }
    
    cout << max_lie;

    return 0;
}

// https://usaco.org/index.php?page=viewproblem2&cpid=1228
