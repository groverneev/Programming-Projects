#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("herding.in", "r", stdin);
	freopen("herding.out", "w", stdout);

    vector<int> v(3);

    for (int& i : v) {
        cin >> i;
    }

    sort(v.begin(), v.end());

    // To find minimum, divide into cases: either 0, 1, or 2

    if (v[0] + 1 == v[1] && v[1] + 1 == v[2]) {
        cout << 0 << "\n";
    } else if ((v[1] == v[2] - 2) || (v[0] == v[1] - 2)) {
        cout << 1 << "\n";
    } else {
        cout << 2 << "\n";
    }

    // To find max, find the largest difference between end and middle, minus one
    cout << max(v[2] - v[1], v[1] - v[0]) - 1;
    return 0;
}
