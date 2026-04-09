#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
// vector<int> numbers;
// printf('hello');
// int numofnumbers;
// scanf('%d', &numofnumbers);

int main() {
    int numofnumbers;
    scanf("%d", &numofnumbers);
    vector<int> gifts;
    gifts.reserve(numofnumbers);
    int num;
    for (int i=0;i<numofnumbers;i++) {
        scanf("%d", &num);
        gifts.push_back(num);
    }
    std::sort(gifts.begin(), gifts.end());
    int mid = numofnumbers / 2;
    int donenum = mid - 1;
    int done[numofnumbers];
    int donei = 0;
    for (int i=0;i<(int) (numofnumbers / 2); i++) {
        done[donei++] = gifts[i];
        done[donei++] = gifts[mid+i];
    }
    if (numofnumbers % 2 == 1) {
        done[numofnumbers - 1] = gifts[numofnumbers - 1];
        donenum++;
    }
    printf("%d\n", donenum);
    for (int i =0;i<numofnumbers;i++) {
        printf("%d ", done[i]);
    }

    // printf("%d %d ", )
    return 0;
}