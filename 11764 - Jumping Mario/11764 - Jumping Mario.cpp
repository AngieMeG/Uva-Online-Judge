#include <bits/stdc++.h>
using namespace std;
int main(){
    //freopen("out.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    for (int i = 1; i <= cases; i++){
        int high = 0,low = 0,walls;
        scanf("%d",&walls);
        int lis[walls];
        for (int k = 0; k < walls; k++){
            scanf("%d",&lis[k]);
            if (k > 0){
                if(lis[k-1] < lis[k]){high++;}
                else if(lis[k-1] > lis[k]){low++;}
            }
        }
        printf("Case %d: %d %d\n",i,high,low);
    }
    return 0;
}
