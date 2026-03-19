#include <iostream>  // for std::cout and std::cin
using namespace std;

int main()
{
    std::cout << "Enter a number: "; // ask user for a number

    int x{};       // define variable x to hold user input (and value-initialize it)
    std::cin >> x; // get number from keyboard and store it in variable x

    std::cout << "You entered " << x << '\n';

    cout << "Enter two numbers:";
    int a{}; // define variable a to hold user input (and value-initialize it)
    int b{}; // define variable b to hold user input (and value-initialize it)
    std::cin >> a >> b; // get two numbers and store in variable a and b respectively

    std::cout << "You entered " << a << " and " << b << '\n';

    return 0;
}
