#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen("outofplace.in", "r", stdin);
	freopen("outofplace.out", "w", stdout);

    int n;
    cin >> n;

    vector<int> unsorted(n);
    for (int& i : unsorted) {
        cin >> i;
    }
    // This algorithm was created by claude, as I couldn't figure it out
    // Issue: I did not read the question properly: only one cow moved, so obviously the number of swaps was the difference - 1
    vector<int> solution = unsorted;
    sort(solution.begin(), solution.end());

    int diff{};
    for (int i = 0; i < n; ++i) {
        if (unsorted[i] != solution[i]) {
            ++diff;
        }
    }

    if (diff != 0) {
        cout << diff - 1;
    }
    else {
        cout << 0;
    }

    return 0;
}
