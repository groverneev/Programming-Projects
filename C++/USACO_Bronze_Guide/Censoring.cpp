#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("censor.in");
    ofstream fout("censor.out");

    string s, t;
    fin >> s >> t;
    int index{};
    while (s.find(t, index) != std::string::npos)
    {
        index = s.find(t, index);
        
        // s = s.substr(0, index) + s.substr(index + t.size());
        // previous line is inefficient; claude suggested a better line:
        s.erase(index, t.size());

        index -= t.size() + 1;
        if (index < 0) { index = 0; }
    }
    
    fout << s;

    return 0;
}
