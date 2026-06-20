#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    long long n;
    cin >> n;
    vector<long long> v(n);
    for (auto& i : v) {
        cin >> i;
    }

    sort(v.begin(), v.end());


    long long max_profit{};
    long long charge{};

    for (const auto& i : v) {
        long long s = i * n;
        if (s > max_profit) {
            max_profit = s;
            charge = i;
        }
        n--;
    }

    cout << max_profit << " " << charge;

    return 0;
}
