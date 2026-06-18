#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("circlecross.in");
    ofstream fout("circlecross.out");

    vector<char> v = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int counter{};

    string s;
    fin >> s;
    
    for (const char& c : v) {
        set<char> stuffToCount;
        int i = s.find(c) + 1;
        int f = s.rfind(c); // Searches the string in reverse
        for (i; i < f; i++) {
            char ins = s[i];
            if (stuffToCount.erase(ins) == 0) {
                stuffToCount.insert(ins);
            }
        }
        counter += (int) stuffToCount.size();
    }


    fout << counter / 2; // Double counted intersections
    return 0;
}
