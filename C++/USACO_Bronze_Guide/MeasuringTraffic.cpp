#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("traffic.in");
    ofstream fout("traffic.out");

    int n;
    fin >> n;

    vector<tuple<string, int, int>> v;
    string a;
    int b, c;
    int low{0};
    int high{10000000}; // these bounds are much safer as int won't overflow now
    for (int i = 0; i < n; i++) {
        fin >> a >> b >> c;
        v.push_back(make_tuple(a, b, c));

        if (a == "none") {
            low = max(b, low);
            high = min(high, c);
        }

        else if (a == "off") {
            low -= c;
            high -= b;
        }

        else if (a == "on") {
            low += b;
            high += c;
        }

        low = max(low, 0); // flow rate can never be negative; implicit bounds!!
    }

    int ans1, ans2;
    ans1 = low;
    ans2 = high;

    low = 0;
    high = 1000000;

    for (int i = v.size() - 1; i >= 0; i--) {
        tuple<string, int, int> thing = v[i];
        a = (string) get<0>(thing);
        b = (int) get<1>(thing);
        c = (int) get<2>(thing);

        if (a == "none") {
            low = max(b, low);
            high = min(high, c);
        }
        // issue: operations are reversed for off ramps
        else if (a == "off") {
            low += b;
            high += c;
        }

        else if (a == "on") {
            low -= c;
            high -= b;
        }

        low = max(low, 0); // flow rate can never be negative; implicit bounds!!
    }

    fout << low << ' ' << high << "\n" << ans1 << ' ' << ans2;

    return 0;
}
