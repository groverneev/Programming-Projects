//#include <iostream>
//#include <vector>
//#include <climits>
#include <bits/stdc++.h> // This header pulls in the entire standard library at once
using namespace std;

// High quality program finding the max of a group of numbers and the sum of those numbers

int main() {
    ios_base::sync_with_stdio(false); // turns off sync with scanf / printf -- do not use these
    cin.tie(NULL); // IMPORTANT unlinks cin from cout (now cout isn't flushed every time cin is read)

    int n;
    cin >> n;
    vector<int> v(n);
    long long sum{};
    int max_val = INT_MIN;

    for (int& i : v) {
        cout << "Enter a number";
        cin >> i;
        if (i > max_val) max_val = i;
        sum += i;
    }

    cout << sum << ", " << max_val << "\n";
    return 0;
}
