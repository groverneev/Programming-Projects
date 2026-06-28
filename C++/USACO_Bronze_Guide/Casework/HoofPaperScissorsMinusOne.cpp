#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<string> vec;
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        vec.push_back(s);
    }

    int s1, s2, k;
    for (int test = 0; test < m; ++test) {
        cin >> s1 >> s2;
        --s1; --s2;
        k = 0; // k = number of killer symbols: if bessie has either, then she wins

        for (int i = 0; i < n; ++i) { // i has to beat both of Elsie's symbols
            bool num1 = false, num2 = false; // vec[r][c] == 'W' means "r beats c", and vec[r][c] == 'L' means "r loses to c".
            if (s1 <= i && vec[i][s1] == 'W') { // I confused some of the statements
                // If i > s, then you read [i][s], and you want it to win
                num1 = true;
            }
            else if (s1 > i && vec[s1][i] == 'L') { // This should be L, not W (claude)
                // this cell is flipped (stored from s's perspective), so you have to flip it
                num1 = true;
            }
            if (s2 <= i && vec[i][s2] == 'W') {
                num2 = true;
            }
            else if (s2 > i && vec[s2][i] == 'L') {
                num2 = true;
            }
            if (num1 && num2) {
                ++k;
            }
        }
        cout << n*n - (n - k)*(n - k) << "\n"; // this logic was originally wrong, fixed by claude
        // there are n*n total pairs possible that bessie can hold
        // either L or R has to be a killer; subtract the pairs that aren't this
        // there are n-k non killer symbols, so multiply those and subtract
    }

    return 0;
}
