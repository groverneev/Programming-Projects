#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("angry.in");
    ofstream fout("angry.out");

    // Some issue making it only get 8/10

    int n;
    fin >> n;

    vector<int> v(n);
    for (auto& i : v) {
        fin >> i;
    }

    sort(v.begin(), v.end());

    int maxExplosionCount{};

    for (int i = 0; i < n; i++) {
        int lowIndex{i}, highIndex{i}, t{1}, explosionCount{1};
        
        while ((lowIndex != 0 && v[lowIndex - 1] + t >= v[lowIndex]) || (highIndex != n - 1 && v[highIndex] + t >= v[highIndex + 1])) {
            while (lowIndex != 0 && v[lowIndex - 1] + t >= v[lowIndex]) {
                explosionCount++;
                lowIndex--;
            }
            
            while (highIndex != n - 1 && v[highIndex] + t >= v[highIndex + 1]) {
                explosionCount++;
                highIndex++;
            }

            t++;
        }

        maxExplosionCount = max(explosionCount, maxExplosionCount);
    }

    fout << maxExplosionCount;

    return 0;
}
