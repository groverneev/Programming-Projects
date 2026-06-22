#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// https://cses.fi/problemset/task/1623
// Partially looked at solution to solve (first recursion problem)

ll n;
vector<ll> v;

ll findMinDifference(ll index, ll firstBucketSum, ll secondBucketSum) {
    if (index == n) {
        return abs(firstBucketSum - secondBucketSum);
    }

    return min(findMinDifference(index + 1, firstBucketSum + v[index], secondBucketSum), findMinDifference(index + 1, firstBucketSum, secondBucketSum + v[index]));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;

    v.resize(n);
    for (auto& i : v) {
        cin >> i;
    }

    sort(v.begin(), v.end());

    // Need to use recursion to find all subsets

    cout << findMinDifference(0, 0, 0);

    return 0;
}
