#include <iostream>
#include <cmath>

using namespace std;

const std::string CHARS[5] = {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};

int end_of_loop(int n, int oldval) {
    if (n == -1)  return 0;
    return 5*pow(2, n) + oldval;
}
int end_of_loop(int n) {
    if (n == -1)  return 0;
    return 5*pow(2, n) + end_of_loop(n - 1);
}

int length(int n) {
    return 5*pow(2, n);
}

int main() {
    std::string n;
    std::getline(std::cin, n);
    int num = std::stoi(n);
    int pp=0;
    int olval =0;
    int val;
    while (true) {
        val = end_of_loop(pp, olval);
        if (val >= num) {
            break;
        }
        olval = val;
        pp +=1;
    }
    int start = olval + 1;
    int l = length(pp);
    int offset = num - start;
    int split = l / 5;
    std::string character = CHARS[offset / split];
    std::cout << character;
    return 0;
}