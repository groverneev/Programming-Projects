#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Claude's Idea: S = sum, which is a constant. We want to finish with k numbers, doing N - k merges
    // Goal is to minimize k, so we want to find the smallest target t that works for everything
    // Target t works if you can slice the array into chunks where every chunk adds to t

    // Solved with massive help from Claude for algorithm and debugging

    int num_test_cases;
    cin >> num_test_cases;
    for (int _ = 0; _ < num_test_cases; _++) {

        int N;
        cin >> N;
        vector<int> arr(N);
        int S{};

        for (int& i : arr) {
            cin >> i;
            S += i;
        }

        // Edge case
        if (S == 0) { cout << 0 << "\n"; }

        vector<int> factors;

        for (int i = 1; i*i <= S; i++) { // Sqrt time complexity to find factors; optimization not needed but why not
            // Claude: I have to do i*i <= S to include i = sqrt S as a factor and to ensure there aren't any sqrt decimal rounding issues
            if (S % i == 0) {
                factors.push_back(i);

                if (i != S / i) { // Add matching distinct pair factor (sqrt N time complexity algo for factors)
                    factors.push_back(S / i);
                }
            }
        }

        sort(factors.begin(), factors.end());

        for (int factor : factors) {
            int num_merges{};

            int sum{};
            int counter{};

            bool go = true;

            for (int i : arr) {
                counter++;
                sum += i;

                if (sum > factor) {
                    go = false;
                    break; // Don't need to be in the loop anymore; optimization
                }
                else if (sum == factor) { // Reset
                    sum = 0;
                    num_merges += counter - 1;
                    counter = 0;
                }
            }

            if (go && sum == 0) { // Check for sum == 0 meaning the end is also a perfect block
                cout << num_merges << "\n"; // Make sure to have a "\n" !!!
                break; // Leave the loop b/c you are done with this test case
            }
        }
    }

    return 0;
}
