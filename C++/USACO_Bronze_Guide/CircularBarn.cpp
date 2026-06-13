#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("cbarn.in");
    ofstream fout("cbarn.out");

    int n;
    fin >> n;
    vector<int> v;

    int test;
    int numCows{};
    for (int i = 0; i < n; i++) {
        fin >> test;
        numCows += test;
        v.push_back(test);
    }

    int finalAns{INT_MAX};
    for (int i = 0; i < n; i++) {
        int total{};
        int done{};
        for (int j = 0; j < n; j++) {
            int pos{j + i};
            if (pos >= n) { pos -= n; }
            total += numCows - done;
            done += v[pos];
        }
        finalAns = min(total, finalAns);
    }

    fout << finalAns - numCows;

    return 0;
}
