#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen("breedflip.in", "r", stdin);
	freopen("breedflip.out", "w", stdout);

    int n;
    cin >> n;
    string before;
    cin >> before;
    string after;
    cin >> after;

    bool alreadyFlipped = false;
    int flipCounter{};

    for (int i = 0; i < n; ++i) {
        if (before[i] != after[i]) {
            if (!alreadyFlipped) {
                ++flipCounter;
                alreadyFlipped = true;
            }
        }
        else {
            alreadyFlipped = false;
        }
    }

    cout << flipCounter;

    return 0;
}
