#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen("factory.in", "r", stdin);
	freopen("factory.out", "w", stdout);

    int n;
    cin >> n;

    vector<set<int>> vec(105);

    for (int i = 1; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        vec[b].insert(a);
    }

    for (int i = 1; i <= n; ++i) {
        set<int> addingSet;
        set<int> spotsVisited;
        spotsVisited.insert(i);
        for (const int& num : vec[i]) {

        }
    }

    // resources
    // https://usaco.org/index.php?page=viewproblem2&cpid=940
    // https://csacademy.com/app/graph_editor/
    // cph graphs --- https://usaco.guide/CPH.pdf#page=119
    // https://apps.uworld.com/courseapp/collegeprep/v62/createtest/16670785
    // https://blog.prepscholar.com/sat-vocabulary-words
    // https://tableau.calstate.edu/views/Application_withsystemwide/AppAdmitEnroll?iframeSizedToWindow=true&%3Aembed=y&%3AshowAppBanner=false&%3Adisplay_count=no&%3Arender=true&%3AshowVizHome=no&%3Aorigin=viz_share_link
    // https://www.universityofcalifornia.edu/about-us/information-center/admissions-source-school

    cout << -1;

    return 0;
}
