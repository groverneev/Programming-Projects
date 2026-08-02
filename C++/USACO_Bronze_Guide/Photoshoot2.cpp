#include <bits/stdc++.h>
using namespace std;

// Done all by myself

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> start(n);
    vector<int> end(n);

    for (int& i : start) {
        cin >> i;
    }

    for (int& i : end) {
        cin >> i;
    }

    int startIdx{};
    int endIdx{};
    set<int> mySet;
    int counter{};

    while (startIdx < n && endIdx < n) {
        if (start[startIdx] == end[endIdx]) {
            ++startIdx;
            ++endIdx;
        }
        else if (mySet.find(start[startIdx]) != mySet.end()) {
            ++startIdx;
        }
        else if (start[startIdx] != end[endIdx]) {
            ++counter;
            mySet.insert(end[endIdx]);
            ++endIdx;
        }
    }

    cout << counter;

    return 0;
}
