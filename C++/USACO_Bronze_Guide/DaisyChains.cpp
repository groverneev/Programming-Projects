#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    int v_size = static_cast<int>(v.size());

    int counter = v_size;

    for (int i = 0; i < v_size - 1; i++) {
        for (int j = i + 1; j < v_size; j++) {
            int sum{};
            for (int z = i; z <= j; z++) { sum += v[z]; }
            int x = j - i + 1;
            if (sum%x == 0) {
                sum /= x;
                bool thing = false;
                for (int z = i; z <= j; z++) { thing = true; cout << i << " " << j << "\n"; }
                if (thing) { counter++; }
            }
        }
    }

    cout << counter;

    return 0;
}
