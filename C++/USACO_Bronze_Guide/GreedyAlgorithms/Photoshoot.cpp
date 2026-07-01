#include <bits/stdc++.h>
using namespace std;

vector<bool> vec;

int main() { // claude solution, none of this is my work
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    string s;
    cin >> n >> s;
    int m = n / 2;

    // For each pair, what do we need?
    // 1 = needs a flip (GH)
    // 0 = no flip needed (HG)
    // -1 = don't care (GG or HH)
    vector<int> t(m);
    for (int i = 0; i < m; i++) {
        char a = s[2*i], b = s[2*i+1];
        if (a == 'G' && b == 'H') t[i] = 1;
        else if (a == 'H' && b == 'G') t[i] = 0;
        else t[i] = -1;
    }

    int cur = 0;      // how many flips so far affect this spot: 0 = even, 1 = odd
    int count = 0;
    for (int i = m - 1; i >= 0; i--) {
        if (t[i] == -1) continue;        // don't care, skip

        if (t[i] != cur) {               // wrong state -> need a flip here
            count++;
            if (cur == 0) cur = 1;       // toggle cur between 0 and 1
            else cur = 0;
        }
    }

    cout << count << "\n";
    return 0;
}
