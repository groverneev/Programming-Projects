#include <bits/stdc++.h>
using namespace std;

int main() {
    string fileName = "notlast";
    ifstream fin(fileName + ".in");
    ofstream fout(fileName + ".out");

    int n;
    fin >> n;

    map<string, int> myMap {{"Bessie", 0}, {"Elsie", 0}, {"Daisy", 0}, {"Gertie", 0}, {"Annabelle", 0}, {"Maggie", 0}, {"Henrietta", 0}};

    for (int i = 0; i < n; i++) {
        string s; int amnt;
        fin >> s;
        fin >> amnt;
        myMap[s] += amnt;
    }

    // Code to find second min (below) is awful; gets one test case wrong (empty file)
    // Learning: always come up with algorithm before implementation

    vector<int> v;
    for (const pair<string, int>& p : myMap) {
        v.push_back(p.second);
    }
    sort(v.begin(), v.end());

    int min = v[0];
    int second_min = v[0];
    for (const int& i : v) {
        if (min == second_min && i > min) {
            second_min = i;
        }
        else if (second_min > min && i == second_min) {
            fout << "Tie";
            return 0;
        }
        else if (second_min > min && i > second_min) {
            // find the cow's name that is associated with second_min (only one exists)
            for (const auto& p : myMap) {
                if (p.second == second_min) {
                    fout << p.first;
                    return 0;
                }
            }
        }
    }
    if (min == second_min) {
        fout << "Tie";
    }
    return 0;
}
