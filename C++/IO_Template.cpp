#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("shell.in");
    ofstream fout("shell.out");

    int n;
    fin >> n;
    int a, b, c;
    fin >> a >> b >> c;
    fout << a + b;

    return 0;
}
