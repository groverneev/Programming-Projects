#include <iostream>
using namespace std;

int main() {
    cout << "Enter your number: ";
    int s {};
    cin >> s;
    if (s%2 == 0) {
        cout << "Your number is even";
    }
    else {
        cout << "Your number is odd";
    }
    return 0;
}
