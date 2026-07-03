#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen("lineup.in", "r", stdin);
	freopen("lineup.out", "w", stdout);

    int n;
    cin >> n;

    vector<vector<string>> vec {{"Beatrice"}, {"Bella"}, {"Belinda"}, {"Bessie"}, {"Betsy"}, {"Blue"}, {"Buttercup"}, {"Sue"}};

    for (int test = 0; test < n; ++test) {
		string cow1;
		string cow2;
		string trash;
		cin >> cow1 >> trash >> trash >> trash >> trash >> cow2;

        for (int i = 0; i < 8; ++i) {
            if (vec[i][0] == cow1) {
                vec[i].push_back(cow2);
            } else if (vec[i][0] == cow2) {
                vec[i].push_back(cow1);
            }
        }
    }

    vector<string> output;

    map<string, bool> cowMap = {{"Bessie", 0}, {"Buttercup", 0}, {"Belinda", 0}, {"Beatrice", 0}, {"Bella", 0}, {"Blue", 0}, {"Betsy", 0}, {"Sue", 0}};

    for (int i = 0; i < 8; ++i) {
        if (cowMap.at(vec[i][0]) == false) {
            if ((int) vec[i].size() == 1) {
                output.push_back(vec[i][0]);
                cowMap[vec[i][0]] = true;
            }
            else if ((int) vec[i].size() == 2) {
                output.push_back(vec[i][0]);
                cowMap[vec[i][0]] = true;
                if (cowMap.at(vec[i][1]) == false) {
                    output.push_back(vec[i][1]);
                    cowMap[vec[i][1]] = true;
                }
            }
            else if ((int) vec[i].size() == 3) {

            }
        }
    }

    for (string s : output) {
        cout << s << "\n";
    }

    // Program needs to be finished (not working yet)

    return 0;
}
