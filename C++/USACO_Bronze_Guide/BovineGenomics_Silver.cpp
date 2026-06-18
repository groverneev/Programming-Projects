#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("cownomics.in");
    ofstream fout("cownomics.out");

    // Claude's tip: 3 positions are an accurate predictor if and only if no spotty and plain cows have the same geonomes (in order of course)

    int n, m;
    fin >> n >> m;
    vector<string> spotty(n);
    vector<string> plain(n);
    for (string& s : spotty) {
        fin >> s;
    }
    for (string& s : plain) {
        fin >> s;
    }

    int counter{};

    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            for (int k = j + 1; k < m; k++) {
                bool increase = true;
                for (int a = 0; a < n; a++) {
                    for (int b = 0; b < n; b++) {
                        if (spotty[a][i] == plain[b][i] && spotty[a][j] == plain[b][j] && spotty[a][k] == plain[b][k]) {
                            increase = false;
                        }
                    }
                    if (increase == false) {
                        a = std::numeric_limits<int>::max() - 5;
                    }
                }
                if (increase) {
                    counter++;
                }
            }
        }
    }

    fout << counter;

    return 0;
}
