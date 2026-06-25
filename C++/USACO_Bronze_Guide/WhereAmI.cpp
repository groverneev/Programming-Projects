#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("whereami.in");
    ofstream fout("whereami.out");

    // Had to debug with claude

    int n;
    fin >> n;
    string s;
    fin >> s;

    for (int i = 1; i <= n; i++) { // has to go up all the way to n (eg. test case "AAAA")
        set<string> mySet;
        bool test = true;
        for (int j = 0; j <= n - i; j++) { // has to be <=
            string str = s.substr(j, i); // don't also name the string to be test (same as the bool var)
            if (mySet.find(str) != mySet.end()) {
                test = false;
            }
            else {
                mySet.insert(str);
            }
        }
        if (test) {
            fout << i;
            return 0;
        }
    }

    return 0;
}
