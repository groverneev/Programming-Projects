#include <iostream>
using namespace std;
#include <vector>

int main() {
    int n;
    cin >> n;

    long long sum{};
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        sum += x;
    }

    cout << sum;

    int n;
    cin >> n;
    vector<int> v(n);              // pre-size to n
    for (int i = 0; i < n; i++) {
        cin >> v[i];              // fill directly
    }

    
    return 0;
}
