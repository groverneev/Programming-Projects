#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen("lineup.in", "r", stdin);
	freopen("lineup.out", "w", stdout);

    int n;
    cin >> n;

        // claude solution
    map<string, vector<string>> adj;
    set<string> cows = {"Bessie","Buttercup","Belinda","Beatrice",
                        "Bella","Blue","Betsy","Sue"};

    for (int i = 0; i < n; ++i) {
        string a, b, trash;
        cin >> a >> trash >> trash >> trash >> trash >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    set<string> used;

    for (string start : cows) {
        if (used.count(start)) continue; // if already used, continue
        if (adj[start].size() >= 2) continue;  // only start from an endpoint //(why >=???????? ((maybe because its possible to say x is adjacent to x)))

        string prev = "", cur = start;
        while (cur != "") {
            cout << cur << "\n";
            used.insert(cur);
            string next = "";
            for (string nb : adj[cur])
                if (nb != prev) next = nb;
            prev = cur;
            cur = next;
        }
    }

    return 0;
}
