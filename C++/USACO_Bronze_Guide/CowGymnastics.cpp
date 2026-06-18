#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("gymnastics.in");
    ofstream fout("gymnastics.out");

    int k, n;
    fin >> k >> n;

    vector<vector<int>> grid(k, vector<int>(n, 0));

    for (vector<int>& v : grid) {
        for (int& i : v) {
            fin >> i;
        }
    }

    int consistent_counter{};
    for (int firstcow = 1; firstcow <= n; firstcow++) {
        for (int secondcow = 1; secondcow <= n; secondcow++) {
            if (firstcow != secondcow) {
                int first_counter{};
                int second_counter{};
                for (int i = 0; i < k; i++) {
                    for (int j = 0; j < n; j++) {
                        if (grid[i][j] == firstcow) { first_counter++; j = 1000000;}
                        else if (grid[i][j] == secondcow) { second_counter++; j = 1000000;}
                    }
                    if (first_counter > 0 && second_counter > 0) { i = 1000000; }
                }
                if (first_counter == 0 || second_counter == 0) { consistent_counter++;
                // cout << first_counter << " " << second_counter << " " << firstcow << " " << secondcow << "\n";
                }
            }
        }
    }

    fout << consistent_counter / 2; // being double counted so need to divide by 2

    return 0;
}
