#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string s;
    cin >> s;

    sort(s.begin(), s.end());
    vector<string> results;

    //results.push_back(s);
    //while (next_permutation(s.begin(), s.end())) {
    //    results.push_back(s);
    //}

    do {
        results.push_back(s);
    } while (next_permutation(s.begin(), s.end())); // This is better because it auto includes the first permutation (the sorted one)


    cout << (int) results.size() << "\n";
    for (string i : results) {
        cout << i << "\n";
    }

    return 0;
}
