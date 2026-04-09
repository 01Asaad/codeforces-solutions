#include <iostream>
#include <cstdio>

using namespace std;
// vector<int> numbers;
// printf('hello');
int main() {
    int numofnumbers;
    scanf("%d", &numofnumbers);
    for (int i=0;i<numofnumbers;i++) {
        int length, k;
        scanf("%d %d", &length, &k);
        char stripes_arr[length];
        scanf("%s", stripes_arr);
        // string stripes = stripes_arr;
        int whites = 0;
        for (int j=0;j<k;j++) {
            if (stripes_arr[j] == 'W') {whites +=1;}
        }
        int min_whites = whites;
        int start = 0;
        int end = k - 1;
        for (int i=k;i<length;i++) {
            end++;
            if (stripes_arr[start] == stripes_arr[i]) {}
            else if (stripes_arr[start] == 'W') {whites--;}
            else whites++;
            start++;
            min_whites = min(min_whites, whites);
        }
        printf("%d\n", min_whites);
    }
    
    return 0;
}