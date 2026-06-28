#include <bits/stdc++.h>
using namespace std;

vector<pair<int, bool>> vec(1e5 + 5);


// problem is too difficult and I needed too much help, so I give up



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    string breeds;
    cin >> breeds;

    int test;
    for (int i = 1; i <= n; ++i) {
        cin >> test;
        vec[i].first = test;
        if (breeds[i - 1] == 'G') {
            vec[i].second = false;
        } else {
            vec[i].second = true;
        }
    }
    
    breeds = "";

    int firstTrue{-9}; // Claude's Idea
    int lastTrue{-9};
    int firstFalse{-9};
    int lastFalse{-9};
    
    for (int i = n; i >= 1; --i) {
        if (vec[i].second && lastTrue == -9) {
            lastTrue = i;
        }
        else if (!vec[i].second && lastFalse == -9) {
            lastFalse = i;
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (vec[i].second && firstTrue == -9 && vec[i].first >= lastTrue) {
            firstTrue = i;
        }
        else if (!vec[i].second && firstFalse == -9 && vec[i].first >= lastFalse) {
            firstFalse = i;
        }
    }

    bool True = (vec[firstTrue].first >= lastTrue);
    bool False = (vec[firstFalse].first >= lastFalse);

    int finalCount{};

    if (True) {
        for (int i = 1; i <= n; ++i) {
            if (!vec[i].second && vec[i].first >= firstTrue && i <= firstTrue) {
                finalCount++;
            }
        }
    }

    if (False) {
        for (int i = 1; i <= n; ++i) {
            if (vec[i].second && vec[i].first >= firstFalse && i <= firstFalse) {
                finalCount++;
            }
        }
    }

    if (True && False) {
        bool gCoversH = (firstFalse <= firstTrue && vec[firstFalse].first >= firstTrue);
        bool hCoversG = (firstTrue <= firstFalse && vec[firstTrue].first >= firstFalse);
        if (!gCoversH && !hCoversG) finalCount++;
    }

    cout << finalCount;

    return 0;
}
