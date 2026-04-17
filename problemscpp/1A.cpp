#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#define REP(i,start,end,step) for (int i = start; i < end; i+=step)
 
using namespace std;
 
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m, a;
    scanf("%d %d %d", &n, &m, &a);
    printf("%lld", (long long)(ceil((double)n/a) * ceil((double)m/a)));
    return 0;
}