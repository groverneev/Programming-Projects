#include <bits/stdc++.h>
using namespace std;

vector<set<int>> vec(105);

void recurse(int x, set<int>& spots) {
    for (const int& i : vec[x]) {
        auto result = spots.insert(i);
        if (result.second == true) { // not duplicate 
            recurse(i, spots);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen("factory.in", "r", stdin);
	freopen("factory.out", "w", stdout);

    int n;
    cin >> n;

    for (int i = 1; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        vec[b].insert(a); // in b's list, we see that a is going into it
    }

    for (int i = 1; i <= n; ++i) {
        set<int> spotsVisited;
        spotsVisited.insert(i);
        recurse(i, spotsVisited);
        if (spotsVisited.size() == n) {
            cout << i;
            return 0;
        }
    }

    cout << -1;

    // https://csacademy.com/app/graph_editor/
    // cph graphs --- https://usaco.guide/CPH.pdf#page=119
    // https://apps.uworld.com/courseapp/collegeprep/v62/createtest/16670785
    // https://blog.prepscholar.com/sat-vocabulary-words
    // https://tableau.calstate.edu/views/Application_withsystemwide/AppAdmitEnroll?iframeSizedToWindow=true&%3Aembed=y&%3AshowAppBanner=false&%3Adisplay_count=no&%3Arender=true&%3AshowVizHome=no&%3Aorigin=viz_share_link
    // https://www.universityofcalifornia.edu/about-us/information-center/admissions-source-school

    return 0;
}
