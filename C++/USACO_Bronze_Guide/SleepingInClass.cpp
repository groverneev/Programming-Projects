#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    for (int _ = 0; _ < t; _++) {



        int n;
        cin >> n;
        vector<int> v(n);
        for (int& i : v) {
            cin >> i;
        }

        int modification_counter{}; // use this var 
        bool test = true;
        while (test) {
            int max{v[0]}; // use this var

            bool allSame = true;
            int same = v[0];
            for (const int& i : v) {
                if (i > max) {
                    max = i;
                }
                if (i != same) {
                    allSame = false;
                }
            }
            if (allSame == false) {
                test = false;
            }
            if (test == true) {
                for (int i = 0; i < (int) v.size(); i++) {
                    // do something
                }
            }
        }

        cout << modification_counter << "\n";




    }

    return 0;
}
