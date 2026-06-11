#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("shell.in");
    ofstream fout("shell.out");

    int n;
    fin >> n;

    int one{};
    int two{};
    int three{};

    int pos1{1};
    int pos2{2};
    int pos3{3};

    int a, b, g;
    for (int i = 0; i < n; i++) {
        fin >> a >> b >> g; // these 3 checks can be simplified with a loop, but besides that the solution is great
        if (pos1 == a) { pos1 = b; } else if (pos1 == b) { pos1 = a; }
        if (pos2 == a) { pos2 = b; } else if (pos2 == b) { pos2 = a; }
        if (pos3 == a) { pos3 = b; } else if (pos3 == b) { pos3 = a; }
        
        if (pos1 == g) one++;
        if (pos2 == g) two++;
        if (pos3 == g) three++;
    }

    int answer = max({one, two, three});
    fout << answer;

    return 0;
}
