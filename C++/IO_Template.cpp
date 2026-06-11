#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("shell.in");
    ofstream fout("shell.out");

    int n;
    fin >> n;

    for (int i = 0; i < n; i++) {
        int a, b, g;
        fin >> a >> b >> g;
    }

    int answer = 0;
    fout << answer;

    return 0;
}
