#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N;
    cin >> M;

    vector<vector<int>> cows(N);
    vector<vector<int>> ACs(M);

    int a, b, c, d;
    for (vector<int> v : cows) {
        cin >> a >> b >> c;
        v.push_back(a);
        v.push_back(b);
        v.push_back(c);
    }
    for (vector<int> v : ACs) {
        cin >> a >> b >> c >> d;
        v.push_back(a);
        v.push_back(b);
        v.push_back(c);
        v.push_back(d);
    }

// need to continue this program

    return 0;
}
