#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Key learning: always use long long!!!

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    ll n, q;
    cin >> n >> q;
    vector<ll> vec(n + 4, 0);
    vector<ll> prefix(n + 4, 0);
    ll asdf;
    for (ll i = 1; i <= n; ++i) {
        cin >> asdf;
        vec[i] = asdf;
        prefix[i] = prefix[i - 1] + asdf;
    }

    ll l, r;

    for (ll i = 0; i < q; ++i) {
        cin >> l >> r;
        cout << prefix[r] - prefix[l] << "\n";
    }


    return 0;
}

// https://codeforces.com/contest/1398/problem/C