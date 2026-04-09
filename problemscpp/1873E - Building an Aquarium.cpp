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
    int testcases;
    scanf("%d", &testcases);
    for (int i=0;i<testcases;i++) {
        int columnlen;int maxw;
        scanf("%d %d", &columnlen, &maxw);
        int cols[columnlen];
        for (int j=0;j<columnlen;j++) {
            scanf("%d", &cols[j]);
        }
        std::sort(cols, cols+columnlen);
        
        long long subtract[columnlen];
        subtract[0] = cols[0];
        for (int pp=1;pp<columnlen;pp++) {
            subtract[pp] = cols[pp] + subtract[pp-1];
        }
        
        long long h=0;
        bool broken = false;
        long long w;
        for (int pp=0;pp<columnlen;pp++) {
            h = cols[pp];
            w = (1LL * (pp +1) * h) - subtract[pp];
            if (w> maxw) {
                w = (1LL * (pp) * cols[pp-1]) - subtract[pp-1];
                h=cols[pp-1] + (maxw - w)/(pp) + 1;
                broken = true;
                break;
            }
        }
        if (!broken) {
            h=(maxw - w) / columnlen + h + 1; 
        }
        printf("%lld\n", h - 1);
    }
    return 0;
}