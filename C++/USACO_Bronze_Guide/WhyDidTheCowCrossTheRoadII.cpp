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
        for (i; i < (int) s.size(); i++) {
            if (c == s[i]) {
                i = std::numeric_limits<int>::max() - 6;
            }
            else {
                char ins = s[i];
                if (stuffToCount.erase(ins) == 0) {
                    stuffToCount.insert(ins);
                }
            }
        }
        counter += (int) stuffToCount.size();
    }


    fout << counter / 2; // Double counted intersections
    return 0;
}
