// https://cses.fi/problemset/task/1624

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    vector<vector<bool>> grid(8);
    for (vector<bool>& v : grid) {
        for (int i = 0; i < 8; i++) {
            char c;
            cin >> c;
            if (c == '.') { v.push_back(true); }
            else { v.push_back(false); }
        }
    }

    int possibilities{};

    vector<int> v = {0, 1, 2, 3, 4, 5, 6, 7}; // these are the rows the pieces are on

    do {
        bool works = true;

        for (int i = 0; i < 8; i++) {
            if (grid[v[i]][i] == false) { works = false; break; }
        }

        // Need to ensure no two queens are on same diagonal
        // Implemented by Claude
        // Approach: 
        for (int i = 0; i < 8 && works; i++) { // First index of vector v
            for (int j = i + 1; j < 8; j++) { // Second index of vector v
                if (abs(v[i] - v[j]) == abs(i - j)) { // This means they are on a same diagonal
                    works = false;
                    break;
                }
            }
        }

        if (works) {
            possibilities++;
        }
    } while (next_permutation(v.begin(), v.end()));

    cout << possibilities;

    return 0;
}
