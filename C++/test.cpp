#include <iostream>
using namespace std;

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

    return 0;
}
