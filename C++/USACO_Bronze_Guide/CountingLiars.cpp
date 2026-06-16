#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
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

    int min_lie{std::numeric_limits<int>::max()};

    for (pair<bool, int> _ : v) {
        int num_lie{};

        int assumedLocation = _.second;

        for (pair<bool, int> cowsGuesses : v) {
            // Idea: the first loop is giving actual location and we are checking if each cow is consistent with actual loc or not
            // From Claude
            if (!cowsGuesses.first && cowsGuesses.second < assumedLocation) {
                num_lie++;
            }
            else if (cowsGuesses.first && cowsGuesses.second > assumedLocation) {
                num_lie++;
            }
        }
        if (num_lie < min_lie) { min_lie = num_lie; }
    }
    
    cout << min_lie;

    return 0;
}
