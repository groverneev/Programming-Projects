#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("paint.in", "r", stdin);
	freopen("paint.out", "w", stdout);

    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if ((c > a && c > b && d > a && d > b) || (c < a && c < b && d < a && d < b)) {
        cout << b - a + d - c;
    } else {
        cout << max(b, d) - min(a, c);
    }
    
    return 0;
}
