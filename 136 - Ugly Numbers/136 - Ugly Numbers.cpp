#include <bits/stdc++.h>
using namespace std;

int main(){
    int lis[1500];
    lis[0] = 1;
    int f2 = 0, f3 = 0, f5 = 0;
    for (int i = 1; i < 1500; i++){
        lis[i] = min(2 * lis[f2], min(3 * lis[f3], 5 * lis[f5]));
        if (lis[i] == 2 * lis[f2]){f2++;}
        if (lis[i] == 3 * lis[f3]){f3++;}
        if (lis[i] == 5 * lis[f5]){f5++;}
    }
    printf("The 1500'th ugly number is %d.\n", lis[1499]);

    return 0;
}
